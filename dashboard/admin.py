from unicodedata import category
from django.contrib import admin
from .models import Product
from .models import Commande
#from .models import Mystock
from django.contrib.auth.models import Group

admin.site.site_header = 'Espace du gerant'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'quantity', 'critique',)
    

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Commande) 
#admin.site.register(Mystock) 