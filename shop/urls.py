from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    
    path('', views.BoutiqueView.as_view(), name='shop'), 
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('delete-cart-item/<int:pk>/', views.CartView.delete_cart_item, name='delete_cart_item'),
    path('error', views.error, name='error'),
    path('boss', views.boss, name='boss')
    
]

