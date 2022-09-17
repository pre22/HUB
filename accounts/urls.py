from django.urls import path
from accounts.views import ReviewView


urlpatterns = [
    path("reviews/", ReviewView.as_view(), name="review")
]