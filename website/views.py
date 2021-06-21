from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def product_detail(request):
    return render(request, 'product-details.html')

def shop(request):
    return render(request, 'shop.html')
# Create your views here.
