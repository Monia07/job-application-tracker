from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import JobApplicationForm
from .models import JobApplication


@login_required
def application_list(request):
    applications = JobApplication.objects.filter(user=request.user)

    status_filter = request.GET.get("status")

    if status_filter:
        applications = applications.filter(status=status_filter)

    stats = JobApplication.objects.filter(user=request.user).aggregate(
        total_applications=Count("id"),
        interview_count=Count("id", filter=Q(status="interview")),
        offer_count=Count("id", filter=Q(status="offer")),
    )

    return render(
        request,
        "tracker/application_list.html",
        {
            "applications": applications,
            "total_applications": stats["total_applications"],
            "interview_count": stats["interview_count"],
            "offer_count": stats["offer_count"],
            "status_filter": status_filter,
        },
    )


@login_required
def add_application(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            messages.success(request, "Application added successfully.")
            return redirect("application_list")
        messages.error(request, "Please correct the errors below.")
    else:
        form = JobApplicationForm()

    return render(
        request,
        "tracker/add_application.html",
        {"form": form},
    )


@login_required
def edit_application(request, pk):
    application = get_object_or_404(
        JobApplication,
        pk=pk,
        user=request.user,
    )

    if request.method == "POST":
        form = JobApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            messages.success(request, "Application updated successfully.")
            return redirect("application_list")
        messages.error(request, "Please correct the errors below.")
    else:
        form = JobApplicationForm(instance=application)

    return render(
        request,
        "tracker/edit_application.html",
        {"form": form, "application": application},
    )


@login_required
def delete_application(request, pk):
    application = get_object_or_404(
        JobApplication,
        pk=pk,
        user=request.user,
    )

    if request.method == "POST":
        application.delete()
        messages.success(request, "Application deleted successfully.")
        return redirect("application_list")

    return render(
        request,
        "tracker/delete_application.html",
        {"application": application},
    )