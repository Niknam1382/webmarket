from django.db import models

# Create your models here.
class Newsletters(models.Model):
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta :
        ordering = ['-date']

    def __str__ (self) :
        return '{} - {}'.format(self.email, self.date)

class ContactForm(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta :
        ordering = ['-created_date']

    def __str__ (self) :
        return '{} - {}'.format(self.last_name, self.subject)