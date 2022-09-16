from django.contrib import admin
from services.models import Order, ServicePackage
# Register your models here.

admin.site.register(Order),
admin.site.register(ServicePackage)