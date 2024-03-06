from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.http import JsonResponse


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')  

def shop(request):
    return render(request, 'shop.html')   

def work(request):
    return render(request, 'works.html')     

def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    # Add the product to the cart (not shown)
    # Calculate total price (not shown)
    return JsonResponse({'success': True})



def checkout(request):
    if request.method == 'POST':
        # Retrieve cart items and calculate total price
        # Calculate shipping cost based on shipping address
        # Create an order instance and save it to the database
        return JsonResponse({'success': True})
    else:
        return render(request, 'checkout.html')


# Create your views here.
