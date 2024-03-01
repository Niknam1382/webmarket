# Generated by Django 4.2.9 on 2024-02-29 22:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zarinpal', '0002_rename_total_price_totalprice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='totalprice',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
