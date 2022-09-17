from django.urls import path
from accounts.views import ReviewView


urlpatterns = [
    path("/", ReviewView.as_view(), name="review")
]