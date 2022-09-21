from rest_framework import serializers
from services.models import Order, ServicePackage

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ("id", "offer_title", "description", "address", "date", "price", "business_to", "username",)
        read_only_fields = ["business_to", "username"]


class ServicePackageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServicePackage
        fields = ("id", "package_name", "package_info", "no_of_people", "duration", "average_pricing", "no_of_server", "no_of_dishes", "business")
        read_only_fields = ["business"]