# Generated by Django 4.2.9 on 2024-02-02 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_product_brand_remove_product_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='store.category'),
        ),
    ]
