from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    middle_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "middle_name", "last_name", "password"]

    def __str__(self):
        return self.email
    


class Reviews(models.Model):
    client_username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review_text = models.CharField(max_length=500)
    rating = models.CharField(max_length=50)