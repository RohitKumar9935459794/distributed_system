from django.shortcuts import render, redirect
from .models import User, Product, Order
from .forms import UserForm, ProductForm, OrderForm

def index(request):
    users = User.objects.all()
    products = Product.objects.all()
    orders = Order.objects.all()
    return render(request, 'core/index.html', {'users': users, 'products': products, 'orders': orders})

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'core/add.html', {'form': form, 'type': 'User'})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'core/add.html', {'form': form, 'type': 'Product'})

def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = OrderForm()
    return render(request, 'core/add.html', {'form': form, 'type': 'Order'})
