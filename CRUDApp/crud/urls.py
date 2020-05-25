
from django.contrib import admin
from django.urls import path

from .views import home, products, customers, create_order

urlpatterns = [
    path('', home, name='home'),
    path('products', products, name='products'),
    path('customers/<str:pk_test>/', customers, name='customers'),
    path('create_order', create_order, name='create_order')
]
