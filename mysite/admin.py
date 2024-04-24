from django.contrib import admin
from .models import Product
from .models import Order
from .models import product_view

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('size', 'quantity', 'shipping', 'total_price')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'created_at', 'updated_at')

@admin.register(product_view)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')




# Register your models here.
