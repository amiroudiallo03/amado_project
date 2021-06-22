from django.shortcuts import render
from . import models
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    is_index = True
    articles = models.Article.objects.filter(status=True)
    network = models.SocialNetwork.objects.filter(status=True)
    website = models.Website.objects.filter(status=True).first()
    return render(request, 'index.html', locals())

def cart(request):
    is_cart = True
    website = models.Website.objects.filter(status=True).first()
    return render(request, 'cart.html')

def checkout(request):
    is_checkout = True
    website = models.Website.objects.filter(status=True).first()
    return render(request, 'checkout.html')

def product_detail(request):
    is_product_detail = True
    website = models.Website.objects.filter(status=True).first()
    return render(request, 'product-details.html')

def shop(request):
    is_shop = True
    is_active = True
    website = models.Website.objects.filter(status=True).first()
    return render(request, 'shop.html')

def is_email(email):
    try:
        validate_email(email)
        return True
    except:
        return False

@csrf_exempt
def postmail(request):
    success, message = False, " "
    if request.method =="POST":
        email = json.loads(request.POST.get("email"))
        if email.isspace:
            message = 'remplir les champs'
        elif is_email(email):
            message = 'invalide'
        else:
            newsletter = models.Newsletter(email=email)
            newsletter.save()
            success = True
            message = 'validé'

    data = {
        'success': success,
        'message': message
    }
    return JsonResponse(datas, safe=False)