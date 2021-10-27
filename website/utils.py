import datetime
import os

from .cart import Cart

from .models import Checkout, OrderItem

def checkout(request, first_name, last_name, company_name, email, pays, adresse, ville, zip_code, phone, commentaire):
    order = Checkout(first_name=firstname, last_name=lastname, company_name=companyname, email=email, pays=pays, adresse=adresse, ville=ville, zip_code=zipcode, phone=phone, commentaire=commentaire)
    order.save()

    cart = Cart(request)

    for item in cart:
        OrderItem.objects.create(checkout=order, article=item['article'], quantity=item['quantity']) 

    return order.id