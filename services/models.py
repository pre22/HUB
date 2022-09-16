from django.db import models

STATUS = (
    ("Male", "Male"),
    ("Female", "Female"),
)

class Order(models.Model):
    username =
    offer_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    date = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=STATUS)


class ServicePackage(models.Model):
    package_name = models.CharField(max_length=100)
    package_info = models.CharField(max_length=300)
    no_of_people = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    average_pricing = models.CharField(max_length=50)
    no_of_server = models.CharField(max_length=50)
    no_of_dishes = models.CharField(max_length=50)

