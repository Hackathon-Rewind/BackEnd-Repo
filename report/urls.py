from django.urls import path
from .views import report_endpoint, report_list_endpoint

urlpatterns = [
    path("post/", report_endpoint),
    path("list/", report_list_endpoint),
]