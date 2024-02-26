# Generated by Django 4.2.9 on 2024-02-25 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_cart_product_cart_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisteredCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=255)),
                ('address1', models.TextField()),
                ('address2', models.TextField(blank=True, null=True)),
                ('code_posti', models.IntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.cart')),
            ],
        ),
    ]
