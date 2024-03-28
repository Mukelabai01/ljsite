from django.shortcuts import render, get_object_or_404
from .models import Product
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.http import JsonResponse
from .models import Order
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ProductForm
from decimal import Decimal
from django.http import HttpResponseNotAllowed


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')  
def single(request):
    return render(request, 'single.html')

def product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        size = request.POST['size']
        quantity = int(request.POST['quantity'])
        shipping = request.POST.get('shipping', False)
        total_price = float(request.POST['total_price'])
        # Save the product info in the session
        request.session['product_id'] = product_id
        request.session['size'] = size
        request.session['quantity'] = quantity
        request.session['shipping'] = shipping
        request.session['total_price'] = total_price
        # Redirect to the checkout page
        return redirect(reverse('checkout', kwargs={'product_id': product_id}))
    return render(request, 'product.html', {'product': product})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    request.session['product_id'] = product.id
    request.session['size'] = request.POST.get('size')
    request.session['quantity'] = request.POST.get('quantity')
    request.session['shipping'] = request.POST.get('shipping')
    request.session['total_price'] = request.POST.get('total_price')
    return redirect('checkout')



def calculate_total_price(product, size, quantity, shipping):
    # Define the base price per item based on size
    if size == 'A5':
        base_price = 20
    elif size == 'A4':
        base_price = 40
    elif size == 'A3':
        base_price = 60
    elif size == 'A2':
        base_price = 80
    else:
        # Handle invalid size
        return None

    # Calculate the total price including quantity and shipping
    total_price = (base_price * quantity) + (50 if shipping == 'europe' else 20 if shipping == 'africa' else 0)
    return total_price

    
def contact(request):
    return render(request, 'contact.html')

  

def single1(request):
    return render(request, 'single1.html')

def single2(request):
    return render(request, 'single2.html')  

def single3(request):
    return render(request, 'single3.html')    

def single4(request):
    return render(request, 'single4.html')  

def single5(request):
    return render(request, 'single5.html')   

def single6(request):
    return render(request, 'single6.html')   

def single7(request):
    return render(request, 'single7.html') 

def single8(request):
    return render(request, 'single8.html')    

def single9(request):
    return render(request, 'single9.html') 

def single10(request):
    return render(request, 'single10.html') 

def single11(request):
    return render(request, 'single11.html')          





def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})

def work(request):
    return render(request, 'branding.html')     




def checkout(request, product_id):
    if request.method == 'GET':
        # Handle the GET request for the checkout page
        product_id = request.session.get('product_id')
        size = request.session.get('size')
        quantity = request.session.get('quantity')
        shipping = request.session.get('shipping')
        total_price = request.session.get('total_price')

        if product_id is None:
            # Redirect to the shop page or display an error message
            return redirect('shop')  # Assuming 'shop' is the name of your shop URL pattern

        # Retrieve the product from the database
        product = get_object_or_404(Product, id=product_id)
        # Render the checkout page with the product info
        return render(request, 'checkout.html', {
            'product': product,
            'size': size,
            'quantity': quantity,
            'shipping': shipping,
            'total_price': total_price,
        })
    elif request.method == 'POST':
        # Handle the POST request for processing the checkout
        product_id = request.session.get('product_id')
        if product_id is None:
            # Handle the case where product_id is not in the session
            return redirect('shop')  # Redirect to the shop page or display an error message

        # Use the product_id to fetch product details or process the checkout
        return HttpResponse(f"Checkout for product with ID {product_id}")