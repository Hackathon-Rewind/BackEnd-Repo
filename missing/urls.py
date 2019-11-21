from django.urls import path

from .views import (
    posting_endpoint
)

urlpatterns = [
    path("post/", posting_endpoint),
]
