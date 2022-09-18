from rest_framework import generics
from accounts.models import Reviews
from accounts.serializers import ReviewSerializer

class ReviewView(generics.ListCreateAPIView):
    ''' Handles Create-Review Form and also List the Reviews a Business has'''
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
