import graphene
from graphene_django import DjangoObjectType
from website import models 
from website.models import Categorie



class ArticleType(DjangoObjectType):
    class Meta:
        model = models.Article
        fields = "__all__"

class CategorieType(DjangoObjectType):
    class Meta:
        model = models.Categorie
        fields = "__all__"


class Query(graphene.ObjectType):
    article = graphene.List(ArticleType)
    categorie = graphene.List(CategorieType)
 
    def resolve_article(root, info):
        return models.Article.objects.all()

    def resolve_categorie(root, info):
        return Categorie.objects.all()
        
    

schema = graphene.Schema(query=Query)