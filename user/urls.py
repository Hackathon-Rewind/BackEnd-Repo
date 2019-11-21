from django.urls import path

from .views import (
    signup_endpoint,
    login_endpoint
)

urlpatterns = [
    path("signup/", signup_endpoint),
    path("login/", login_endpoint),
]
