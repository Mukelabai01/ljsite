from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.http import JsonResponse


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')  
def single(request):
    return render(request, 'single.html')


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
    return render(request, 'shop.html')   

def work(request):
    return render(request, 'branding.html')     

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
