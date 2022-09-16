from django.db import models


class Review(models.Model):
    client_username = models.CharField(max_length=50)
    review_text = models.CharField(max_length=500)
    rating = models.CharField(max_length=50)