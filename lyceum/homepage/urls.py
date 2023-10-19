from django.urls import path

from . import views

urlpatterns = [
    path("", views.home),
    path("coffee/", views.show_endpoint_coffee),
]
