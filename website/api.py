from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import json
from django.views.decorators.csrf import csrf_exempt
from website.cart import Cart

from .models import Article

@csrf_exempt
def api_add_to_cart(request):
    data = json.loads(request.body)
    article_id = data['article_id']
    update = data['update']
    quantity = data['quantity']

    cart = Cart(request)

    article = get_object_or_404(Article, pk=article_id)

    if not update:
        cart.add(article=article, quantity=1, update_quantity=False)
    else:
        cart.add(article=article, quantity=quantity, update_quantity=True)
    print(cart)
    jsonresponse = {'success': True}
    return JsonResponse(jsonresponse , safe=False)

def api_increment_quantity(request):
    data = json.loads(request.body)
    jsonresponse = {'success': True}
    article_id = data['article_id']

    cart = Cart(request)

def api_remove_from_cart(request):
    data = json.loads(request.body)
    article_id = str(data['article_id'])
    
    cart = Cart(request)
    cart.remove(article_id)
    jsonresponse = {'success': True}
    return JsonResponse(jsonresponse , safe=False)