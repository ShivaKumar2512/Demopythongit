from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.


def home(request):
    return render(request, 'accounts/dashboard.html')


def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html',{'products':products})


def customers(request):
    customers = Customer.objects.all()
    return render(request, 'accounts/customers.html',{'customers':customers})