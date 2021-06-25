
from django.urls import path
from . import views 
from .api import api_add_to_cart
from .api import api_remove_from_cart

urlpatterns = [
    path('', views.index , name='index'),
    path('cart/', views.cart_detail , name='cart'),
    path('checkout/', views.checkout , name='checkout'),
    path('shop/', views.shop , name='shop'),
    path('product-detail/<int:id>', views.product_detail , name='product-detail'),
    path('postmail/', views.postmail , name='postmail'),
    path('search/', views.searchbar , name='searchbar'),
    path('checkoutpost/', views.checkoutpost , name='checkoutpost'),
    
   #API
    path('api/add_to_cart/', api_add_to_cart , name='api_add_to_cart'),
    path('api/remove_from_cart/', api_remove_from_cart , name='api_remove_from_cart'),
]
