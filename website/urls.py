
from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index , name='index'),
    path('cart/', views.cart , name='cart'),
    path('checkout/', views.checkout , name='checkout'),
    path('shop/', views.shop , name='shop'),
    path('product-detail/<int:id>', views.product_detail , name='product-detail'),
    path('postmail/', views.postmail , name='postmail'),
    path('search/', views.searchbar , name='searchbar'), 
    #path('cart-update/', views.cart_update , name='cart_update'),
]
