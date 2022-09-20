from rest_framework import serializers
from business.models import Business


class BusinessSerializer(serializers.ModelSerializer):

    class Meta:
        model = Business
        fields = ("id", "name", "address", "description", "category", "photo","location",)