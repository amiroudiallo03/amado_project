from django.shortcuts import render, get_object_or_404
from . import models
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse

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
        articles = models.Article.objects.filter(categorie__nom__icontains = category)

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
        if  email.isspace:
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


""" def cart_update(request):
    article_id = request.POST.get("article_id")
    if article_id is not None:
        try:
            article_obj = article.objects.get(id=article_id)
        except article.DoesNotExist:
            print("l'article n'existe plus")
        return redirect("index")
    cart_obj = Cart.objects.new_or_get(request)

    
    new_obj = cart_obj.articles.add(article_obj)  
    added = True

    request.session["cart_items"] = cart_obj.articles.count()
    
    json_data = {
    "added": added,
    "removed": not added,
    }
    return JsonResponse(json_data, safe=False)
    return redirect('index') """