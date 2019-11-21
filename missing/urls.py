from django.urls import path

from .views import (
    posting_endpoint,
    post_list_endpoint,
    post_list_detail_endpoint
)

urlpatterns = [
    path("post/", posting_endpoint),
    path("list/", post_list_endpoint),
    path("list/<int:pk>/", post_list_detail_endpoint),
]
