from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import OrderForm
from .models import *


# Create your views here.


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_orders =orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status = 'Pending').count()

    context = {'orders': orders, 'customers': customers,
               'total_orders':total_orders,
               'delivered':delivered,
               'pending':pending}
    return render(request, 'accounts/dashboard.html', context)


def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})


def customers(request, pk_test):
    print(pk_test)
    customer = Customer.objects.get(id = pk_test)
    orders = customer.order_set.all()
    context = {
        'customer':customer,
        'orders':orders,
        'orders_count':orders.count()
    }
    #print(customer)
    return render(request, "accounts/customers.html",context)


def create_order(request):
    form = OrderForm()
    if request.method == 'POST':
        # print('Printing POST Values',request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
    'form':form
    }
    return render(request,"accounts/order.html",context)