from django.urls import path

from .views import (
    signup_endpoint,
    login_endpoint,
    my_inform_endpoint
)

urlpatterns = [
    path("signup/", signup_endpoint),
    path("login/", login_endpoint),
    path("my/", my_inform_endpoint),
]
