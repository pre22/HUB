from rest_framework import generics
from business.models import Business
from services.models import Order, ServicePackage
from services.serializers import OrderSerializer, ServicePackageSerializer

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
    

class OrderDetailView(generics.RetrieveUpdateAPIView):
    '''Returns detailed view of a business order'''
    queryset =  Order.objects.all()
    serializer_class = OrderSerializer

    # For returning details of order belonging to the business
    def get_queryset(self):
        business_id = self.kwargs.get("business_id")
        queryset = Order.objects.filter(business_to_id=business_id)
        return queryset

    # Updates the order with the supplied pk
    def update(self, request, *args, **kwargs):
        data_to_change = {
            'address': request.data.get("address"),
            'date': request.data.get("date"),
            'price': request.data.get("price")
        }
        # Partial update of the data
        serializer = self.serializer_class(request.user, data=data_to_change, partial=True)
        if serializer.is_valid():
            self.perform_update(serializer)

        return Response(serializer.data)
    

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
        queryset = ServicePackage.objects.filter(business_id=business_id)
        return queryset

    

