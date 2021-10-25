from django.conf import settings

from .models import Article
class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart
    def __iter__(self):
        article_ids = self.cart.keys()
        article_clean_ids = []
        for p in article_ids:
            article_clean_ids.append(p)

            self.cart[str(p)]['article'] = Article.objects.get(pk=p)

        for item in self.cart.values():
            item['total_prix'] = float(item['prix']) * int(item['quantity'])

            yield item
    
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
            

    def add(self, article, quantity=1, update_quantity=False):
        article_id = str(article.id)
        prix = article.prix

        if article_id not in self.cart:
            self.cart[article_id]= {'quantity': 0, 'prix': prix, 'id': article_id}
            
        if update_quantity:
            self.cart[article_id]['quantity'] = quantity
        else:
            self.cart[article_id]['quantity'] = self.cart[article_id]['quantity'] + 1
            
        self.save()

    def remove(self, article_id):
        if article_id in self.cart:
            del self.cart[article_id]
            self.save()
    
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modofied = True


    def get_total_length(self):

        return sum(int(item['quantity']) for item in self.cart.values())

    def get_total_cost(self):
        
        if "total_prix" in self.cart.values():
            return sum(float(item['total_price']) for item in self)
        else:
            return 0
