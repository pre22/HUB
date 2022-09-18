from django.contrib.auth import get_user_model
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from accounts.models import Reviews

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model =  User
        fields = ("id", "email", "firstname", "middlename", "lastname", "password")


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ('id', 'client_username','review_text', 'rating',)