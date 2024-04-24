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

def product(request, pk):
    if request.method == 'POST':
        product = Product.objects.get(id=pk)
        quantity = int(request.POST['quantity'])

        try:
            customer = request.user.customer
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

        # Update the quantity of the existing order item or create a new one
        orderItem.quantity = quantity
        orderItem.save()

        return redirect('cart')

    else:
        product = Product.objects.get(id=pk)
        context = {'product': product}
        return render(request, 'singleproduct.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def cart(request):
    try:
        customer = request.user.customer
    except:
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    order_items = order.orderitem_set.all()  # Retrieve all order items (products) associated with the order

    context = {'order': order, 'order_items': order_items}
    return render(request, 'cart.html', context)

    
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



def store(request):
	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'store.html', context)

def product_view(request, pk):
    if request.method == 'POST':
        product = Product.objects.get(id=pk)
        quantity = int(request.POST['quantity'])

        try:
            customer = request.user.customer
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

        # Update the quantity of the existing order item or create a new one
        orderItem.quantity = quantity
        orderItem.save()

        return redirect('cart')

    else:
        product = Product.objects.get(id=pk)
        context = {'product': product}
        return render(request, 'singleproduct.html', context)



def cart(request):
    try:
        customer = request.user.customer
    except:
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    order_items = order.orderitem_set.all()  # Retrieve all order items (products) associated with the order

    context = {'order': order, 'order_items': order_items}
    return render(request, 'cart.html', context)



