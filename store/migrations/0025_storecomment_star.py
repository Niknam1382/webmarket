# Generated by Django 4.2.9 on 2024-03-09 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_product_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='storecomment',
            name='star',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]