from django.shortcuts import render, get_object_or_404
from . import models
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from website.cart import Cart 

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

    return render(request,'checkout.html')
@csrf_exempt
def checkoutpost(request):
    success, message = False, " "
    if request.method == "POST":
        firstname = request.POST.get("firstName")
        lastname = request.POST.get("lastName")
        companyname = request.POST.get("companyName")
        email = request.POST.get("email")
        pays = request.POST.get("pays")
        adresse = request.POST.get("adresse")
        ville = request.POST.get("ville")
        zipcode = request.POST.get("zipCode")
        phone = request.POST.get("phone")
        commentaire = request.POST.get("commentaire")
        
        checkout = models.Checkout(first_name=firstname, last_name=lastname, company_name=companyname, email=email, pays=pays, adresse=adresse, ville=ville, zip_code=zipcode, phone=phone, commentaire=commentaire)
        checkout.save()
        print("save")
        message = 'validé'
        success = True

        datas={
            'message':message,
            'success': success
        }
        return JsonResponse(datas, safe=False)

def product_detail(request, id):
    is_product_detail = True
    website = models.Website.objects.filter(status=True).first()
    article = get_object_or_404(models.Article, id=id)
    return render(request, 'product-details.html', locals())

def shop(request):
    is_shop = True
    is_active = False
    website = models.Website.objects.filter(status=True).first()
    category = request.GET.get('category')
    if not category:
        articles = models.Article.objects.filter(status=True)
    else:
        cat = get_object_or_404(models.Categorie, id= category)
        articles = cat.categorie_articles.all()


    categories = models.Categorie.objects.filter(status=True).all()
    paginator = Paginator(articles, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    try:
        articles = paginator.page(page_number)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.page_number)

    return render(request, 'shop.html', locals())

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
        if  not email.isspace:
            message = 'remplir les champs'
        elif is_email(email):
            message = 'invalide'
        else:
            newsletter = models.Newsletter(email=email)
            newsletter.save()
            success = True
            message = 'validé'

    datas = {
        'success': success,
        'message': message
    }
    return JsonResponse(datas, safe=False)


def searchbar(request):
    search = request.GET.get('search')
    if not search:
        articles = models.Article.objects.all()
    else:
        articles =  models.Article.objects.filter(nom__icontains=search)
        return render(request, "index.html", locals())


def cart_detail(request):
    is_cart = True
    cart = Cart(request)
    return render(request, 'cart.html', locals())
