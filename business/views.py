from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from business.models import Business
from business.serializers import BusinessSerializer


class BusinessList(generics.ListAPIView):
    ''' Returns List of Business '''
    # var = Business.objects.all()
    # biz = for x in var
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer


class AboutBusiness(generics.RetrieveAPIView):
    ''' Business About Page '''
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    




