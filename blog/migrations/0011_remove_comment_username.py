# Generated by Django 4.2.9 on 2024-03-08 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='username',
        ),
    ]
