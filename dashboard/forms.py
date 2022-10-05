from socket import fromshare
from django import forms
from .models import Commande, Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'quantity']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['product', 'order_quantity']