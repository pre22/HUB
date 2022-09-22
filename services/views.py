from rest_framework import generics
from rest_framework.response import Response
from business.models import Business
from services.models import Order, ServicePackage
from services.serializers import OrderSerializer, ServicePackageSerializer
from HUBAPI.permissions import OwnContent

class OrderView(generics.ListCreateAPIView):
    ''' Handles Create Order form and Order History '''
    # queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # For returning list of order belonging to the business
    def get_queryset(self):
        business_id = self.kwargs.get("business_id")
        queryset = Order.objects.filter(business_to_id=business_id)
        return queryset

    # For setting the value of business_to and username field
    def perform_create(self, serializer):
        us = self.request.user
        id = self.kwargs.get("business_id")
        biz = Business.objects.get(id=id)
        serializer.save(username=us, business_to=biz)
    

class OrderDetailView(generics.RetrieveAPIView):
    '''Returns detailed view of a business order'''
    queryset =  Order.objects.all()
    serializer_class = OrderSerializer

    # For returning details of order belonging to the business
    def get_object(self):
        id = self.kwargs.get("pk")
        business_id = self.kwargs.get("business_id")
        queryset = Order.objects.get(business_to_id=business_id, id=id)
        return queryset

    
class OrderUpdateView(generics.UpdateAPIView):
    '''Updates the a given Order - Order can only be edited by the User that created it'''
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_class = (OwnContent,)


    

class ServicePackageView(generics.ListCreateAPIView):
    ''' Handles Create Service Package form for Business and Business Service List '''
    # queryset = ServicePackage.objects.all()
    serializer_class = ServicePackageSerializer

    def get_queryset(self):
        business_id = self.kwargs.get("business_id")
        queryset = ServicePackage.objects.filter(business_id=business_id)
        return queryset

    def perform_create(self):
        id = self.kwargs.get("business_id")
        biz = Business.objects.get(id=id)
        serializer.save(business=biz)

class ServicePackageDetailView(generics.RetrieveAPIView):
    ''' Returns the service details of a particular business '''
    # queryset = ServicePackage.objects.all()
    serializer_class = ServicePackageSerializer

    def get_queryset(self):
        business_id = self.kwargs.get("business_id")
        queryset = ServicePackage.objects.filter(business=business_id)
        return queryset

    

