# Generated by Django 4.2.9 on 2024-03-09 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0026_product_star_c_alter_product_star'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='star_t',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='star',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]