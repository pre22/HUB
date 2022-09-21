from django.urls import path
from services.views import OrderView, OrderDetailView, ServicePackageView, ServicePackageDetailView

urlpatterns = [
    path("order/", OrderView.as_view()),
    path("order/<int:pk/", OrderDetailView.as_view()),
    path("package/", ServicePackageView.as_view()),
    path("package/details/<int:pk>/", ServicePackageDetailView.as_view())
]
