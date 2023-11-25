from django.urls import path

from . import views

urlpatterns = [
    path("submitForm", views.submitForm, name="index"),
]