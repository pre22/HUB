from django.urls import path
from business.views import BusinessList, AboutBusiness

urlpatterns = [
    path("list/", BusinessList.as_view()),
    path("about/<int:pk>/", AboutBusiness.as_view()),
]