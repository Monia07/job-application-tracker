from django.urls import path
from . import views

urlpatterns = [
    path("", views.application_list, name="application_list"),
    path("add/", views.add_application, name="add_application"),
]