from django.urls import path
from services.views import OrderView, ServicePackageView

urlpatterns = [
    path("order/", OrderView.as_view()),
    path("package/", ServicePackageView.as_view())
]
