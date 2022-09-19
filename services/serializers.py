from rest_framework import serializers
from services.models import Order, ServicePackage

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ("offer_title", "description", "address", "date", "price")


class ServicePackageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServicePackage
        fields = "__all__"