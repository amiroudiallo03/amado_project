from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class Base(models.Model):

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta : 
        abstract = True
        
class Categorie(Base):
    nom = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.nom

class Marque(Base):
    nom = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Marque'
        verbose_name_plural = 'Marques'

    def __str__(self):
        return self.nom


class Article(Base):
    nom = models.CharField(max_length=240)
    image = models.FileField(upload_to="image_articles")
    image_next = models.FileField(upload_to="image_articles")
    prix = models.IntegerField()
    categorie = models.ForeignKey( Categorie, related_name="categorie_articles", on_delete=models.CASCADE)
    marque = models.ForeignKey( Marque, related_name="Marque_articles", on_delete=models.CASCADE)
    description = models.TextField()
    quantite = models.IntegerField()
    favorite = models.BooleanField()
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.nom


class Favorite(Base):
    nom = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'

    def __str__(self):
        return self.nom

class Newsletter(Base):
    email = models.EmailField(max_length=254)

    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletter'

    def __str__(self):
        return self.email

class SocialNetwork(Base):
    nom = models.CharField(max_length=50)
    icone = models.CharField(max_length=50)
    lien = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'SocialNetwork'
        verbose_name_plural = 'SocialNetwork'

    def __str__(self):
        return self.nom


class Checkout(Base):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=150)
    company_name = models.TextField()
    email = models.EmailField(max_length=254)
    pays = models.CharField(max_length=50)
    adresse = models.CharField(max_length=150)
    ville = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    commentaire = models.TextField()

    paid = models.BooleanField(default=False)
    paid_amount = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name = 'Checkout'
        verbose_name_plural = 'Checkouts'

    def __str__(self):
        return self.first_name

class Website(Base):
    description_newsletter = HTMLField()
    nom_site = models.ImageField()
    copyright = models.TextField()

    class Meta:
        verbose_name = 'Website'
        verbose_name_plural = 'Websites'

    def __str__(self):
        return f"self.nom_site"

class Cart(Base):
    produit = models.ForeignKey(Article,related_name="cart_produit", on_delete=models.CASCADE)
    quantite = models.IntegerField()

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Cart'

    def __str__(self):
        return self.produit

class OrderItem(Base):
    checkout = models.ForeignKey('Checkout', related_name='orderitem_checkout',on_delete=models.CASCADE)
    article = models.ForeignKey('Article', related_name='orderitem_article',on_delete=models.CASCADE)
    prix = models.IntegerField()
    quantity = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItem'

    def __str__(self):
        return self.checkout