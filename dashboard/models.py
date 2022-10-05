from django.db import models
from django.contrib.auth.models import User



# Create your models here.

CATEGORY = (
    ('Creme', 'Creme'),
    ('Serum', 'Serum'),
    ('Lait', 'Lait'),
) 

VOLUME = (
    ('50ml', '50ml'),
    ('100ml', '100ml'),
    ('250ml', '250ml'),
    ('500ml', '500ml'),
)

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    price = models.PositiveIntegerField(null=True)
    critique = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)
    volume = models.CharField(max_length=50, choices=VOLUME, null=True)

    def __str__(self):
        return f'{self.category}-{self.name}-{self.volume} '




class Commande(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} ordred by {self.staff.username}'



