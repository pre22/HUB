from django.urls import path
from accounts.views import ReviewView


urlpatterns = [
    path("<int:business_id>/reviews/", ReviewView.as_view(), name="review")
]