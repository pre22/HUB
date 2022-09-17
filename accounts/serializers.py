from rest_framework import serializers
from accounts.models import Reviews

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ('id', 'client_username','review_text', 'rating',)