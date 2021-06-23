from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('image_view','nom','prix','categorie','date_add','date_update','status')
    search_fields = ('nom','prix','categorie')

    def image_view(self, obj):

        return mark_safe(f'<img src="{obj.image.url}" style="width:200px; height:100px">')

@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom','date_add','date_update','status')

@admin.register(models.Marque)
class MarqueAdmin(admin.ModelAdmin):
    list_display = ('nom','date_add','date_update','status')

@admin.register(models.Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('nom','date_add','date_update','status')

@admin.register(models.Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email','date_add','date_update','status')

@admin.register(models.SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('nom','lien','date_add','date_update','status')

@admin.register(models.Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ('list_display','last_name','email','pays','phone','date_add','date_update','status')

@admin.register(models.Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('copyright','nom_site','date_add','date_update','status')

@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('produit',)