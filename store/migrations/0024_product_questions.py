# Generated by Django 4.2.9 on 2024-03-09 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_storecomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='questions',
            field=models.TextField(blank=True, null=True),
        ),
    ]
