# Generated by Django 4.2.9 on 2024-03-01 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='send',
            field=models.BooleanField(default=0),
        ),
    ]