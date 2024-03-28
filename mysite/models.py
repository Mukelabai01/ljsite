from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    size = models.CharField(max_length=10, default='A5')
    quantity = models.IntegerField(default=1)
    shipping = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)



class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name





# Create your models here.
