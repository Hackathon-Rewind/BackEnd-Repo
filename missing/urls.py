from django.urls import path

from .views import (
    posting_endpoint,
    post_list_endpoint,
    post_list_detail_endpoint,
    promotion_endpoint,
    promotion_list_endpoint
)

urlpatterns = [
    path("post/", posting_endpoint),
    path("list/", post_list_endpoint),
    path("list/<int:pk>/", post_list_detail_endpoint),
    path("promotion/<int:pk>/", promotion_endpoint),
    path("promotion/", promotion_list_endpoint),
]
