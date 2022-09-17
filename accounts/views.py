from rest_framework import generics
from accounts.models import Reviews
from accounts.serializers import ReviewSerializer

class ReviewView(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
