from django.shortcuts import render

def application_list(request):
    return render(request, "tracker/application_list.html")

