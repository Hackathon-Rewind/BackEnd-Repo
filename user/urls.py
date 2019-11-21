from django.urls import path

from .views import (
    signup_endpoint
)

urlpatterns = [
    path("signup/", signup_endpoint),
]
