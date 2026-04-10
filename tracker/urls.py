from django.urls import path
from . import views

urlpatterns = [
    path("", views.application_list, name="application_list"),
    path("add/", views.add_application, name="add_application"),
    path("edit/<int:pk>/", views.edit_application, name="edit_application"),
]