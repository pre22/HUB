from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from business.models import Business

class User(AbstractUser):
    email = models.EmailField(unique=True)
    middle_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    


class Reviews(models.Model):
    business_to = models.ForeignKey(Business, on_delete=models.CASCADE)
    client_username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review_text = models.CharField(max_length=500)
    rating = models.CharField(max_length=50)