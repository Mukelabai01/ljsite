from django import views
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('shop/', shop, name='shop'), 
    path('work/', work, name='work'), 
    path('cart/', add_to_cart, name='add_to_cart'),
    path('checkout/', checkout, name='checkout'), 
    ]