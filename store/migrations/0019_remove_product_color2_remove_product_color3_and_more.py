# Generated by Django 4.2.9 on 2024-02-10 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_color2_color3_size2_size3_remove_product_color_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='color3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size3',
        ),
    ]
