from rest_framework import generics
from services.models import Order, ServicePackage
from services.serializers import OrderSerializer, ServicePackageSerializer

class OrderView(generics.ListCreateAPIView):
    ''' Handles Create Order form and Order History '''
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ServicePackageView(generics.ListCreateAPIView):
    ''' Handles Create Service Package form for Business and Business Service List '''
    queryset = ServicePackage.objects.all()
    serializer_class = ServicePackageSerializer

class ServicePackageDetailView(generics.RetrieveAPIView):
    ''' Returns the service details of a particular business '''
    queryset = ServicePackage.objects.all()
    serializer_class = ServicePackageSerializer

    

