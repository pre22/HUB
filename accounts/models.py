from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    middle_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email
    


class Reviews(models.Model):
    client_username = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.CharField(max_length=500)
    rating = models.CharField(max_length=50)