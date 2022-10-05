# Generated by Django 4.1 on 2022-08-31 03:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('quantity', models.PositiveIntegerField(null=True)),
                ('price', models.PositiveIntegerField(null=True)),
                ('critique', models.PositiveIntegerField(null=True)),
                ('category', models.CharField(choices=[('Creme', 'Creme'), ('Serum', 'Serum'), ('Lait', 'Lait')], max_length=50, null=True)),
                ('volume', models.CharField(choices=[('50ml', '50ml'), ('100ml', '100ml'), ('250ml', '250ml'), ('500ml', '500ml')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_quantity', models.PositiveIntegerField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.product')),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
