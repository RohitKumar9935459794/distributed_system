from django import forms
from .models import User, Product, Order

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'product', 'quantity']
