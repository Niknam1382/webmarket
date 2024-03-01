from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TotalPrice(models.Model):
    user = user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.PositiveIntegerField(null=True, blank=True)