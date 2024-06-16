from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    product_name = models.TextField()
    product_image = models.URLField()
    starting_bid = models.IntegerField()
    posted_date = models.DateTimeField(auto_now_add=True)
    ending_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.ending_date:
            self.ending_date = self.posted_date + timedelta(days=7)
        super().save(*args, **kwargs)

class Bids(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    last_updated = models.DateTimeField(auto_now_add=True)