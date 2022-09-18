from rest_framework import generics
from business.models import Business
from business.serializers import BusinessSerializer


class BusinessList(generics.ListAPIView):
    ''' Returns List of Business '''
    # var = Business.objects.all()
    # biz = for x in var
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer


class AboutBusiness(generics.ListAPIView):
    ''' Business About Page '''
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer



