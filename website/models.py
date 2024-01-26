from django.db import models

# Create your models here.
class Newsletters(models.Model):
    email = models.EmailField()

class ContactForm(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField() # first makemigration