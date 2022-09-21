from rest_framework import generics
from accounts.models import Reviews
from accounts.serializers import ReviewSerializer

class ReviewView(generics.ListCreateAPIView):
    ''' Handles Create-Review Form and also List the Reviews a Business has'''
    # queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        business_id = self.kwargs.get("business_id")
        queryset = Reviews.objects.filter(business_to_id=business_id)
        return queryset
    
    def perform_create(self, serializer):
        us = self.request.user
        id = self.kwargs.get("business_id")
        biz = Business.objects.get(id=id)
        serializer.save(client_username=us, business_to_id=biz)

    
