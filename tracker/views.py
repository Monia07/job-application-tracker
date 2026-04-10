from django.shortcuts import render, redirect, get_object_or_404
from .models import JobApplication
from .forms import JobApplicationForm


def application_list(request):
    applications = JobApplication.objects.all()
    return render(
        request,
        "tracker/application_list.html",
        {"applications": applications},
    )


def add_application(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("application_list")
    else:
        form = JobApplicationForm()

    return render(
        request,
        "tracker/add_application.html",
        {"form": form},
    )


def edit_application(request, pk):
    application = get_object_or_404(JobApplication, pk=pk)

    if request.method == "POST":
        form = JobApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect("application_list")
    else:
        form = JobApplicationForm(instance=application)

    return render(
        request,
        "tracker/edit_application.html",
        {"form": form, "application": application},
    )

def delete_application(request, pk):
    application = get_object_or_404(JobApplication, pk=pk)

    if request.method == "POST":
        application.delete()
        return redirect("application_list")

    return render(
        request,
        "tracker/delete_application.html",
        {"application": application},
    )