from django.db import models
from django.conf import settings
from business.models import Business

STATUS = (
    ("Accept", "Accept"),
    ("Declined", "Declined"),
)

class Order(models.Model):
    business_to = models.ForeignKey(Business, on_delete=models.CASCADE) # Business that's recieving the order
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Username of the user creating the order
    offer_title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    date = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=STATUS)

    def __str__(self):
        return self.offer_title
    


class ServicePackage(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    package_name = models.CharField(max_length=100)
    package_info = models.CharField(max_length=300)
    no_of_people = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    average_pricing = models.CharField(max_length=50)
    no_of_server = models.CharField(max_length=50)
    no_of_dishes = models.CharField(max_length=50)

    def __str__(self):
        return self.package_name


