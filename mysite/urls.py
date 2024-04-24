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
    path('product/<int:product_id>/', product, name='product'),
    
   path('checkout/<int:product_id>/', views.checkout, name='checkout'),
   
    path('single/', single, name='single'),
    path('single1/', single1, name='single1'),
    path('single2/', single2, name='single2'),
    path('single3/', single3, name='single3'),
    path('single4/', single4, name='single4'),
    path('single5/', single5, name='single5'),
    path('single6/', single6, name='single6'),
    path('single7/', single7, name='single7'),
    path('single8/', single8, name='single8'),
    path('single9/', single9, name='single9'),
    path('single10/', single10, name='single10'),
    path('single11/', single11, name='single11'),
    path('contact/', contact, name='contact'), 
    path('product1/', product_view, name='product_view'), 
    path('store/', store, name='store'), 
    path('single/', single, name='single'), 
    path('cart/', cart, name='cart'),
    
    
    ]