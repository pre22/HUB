from django.urls import path
from services.views import OrderView, ServicePackageView, ServicePackageDetailView

urlpatterns = [
    path("order/", OrderView.as_view()),
    path("package/", ServicePackageView.as_view()),
    path("package/details/", ServicePackageDetailView.as_view())
]
