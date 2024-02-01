# Generated by Django 4.2.9 on 2024-02-01 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_alter_newsletters_options_remove_newsletters_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsletters',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='newsletters',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
    ]
