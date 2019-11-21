from django.urls import path
from .views import report_endpoint

urlpatterns = [
    path("post/", report_endpoint)
]