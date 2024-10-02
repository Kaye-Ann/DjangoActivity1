from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('products/', views.product, name= 'products'),
    path('cart/', views.carts, name= 'cart')
    
]
