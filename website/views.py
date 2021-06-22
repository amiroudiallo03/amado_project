from django.shortcuts import render


def index(request):
    is_index = True
    return render(request, 'index.html')

def cart(request):
    is_cart = True
    return render(request, 'cart.html')

def checkout(request):
    is_checkout = True
    return render(request, 'checkout.html')

def product_detail(request):
    is_product_detail = True
    return render(request, 'product-details.html')

def shop(request):
    is_shop = True
    return render(request, 'shop.html')
# Create your views here.
