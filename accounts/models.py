from django.db import models
from store.models import product
from django.contrib.auth.models import User
from django.urls import reverse

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # product = models.CharField(max_length=255)
    # product = models.ForeignKey(product, on_delete=models.CASCADE)
    product = models.ManyToManyField(product)
    quantity = models.IntegerField(default=1)
    is_paid = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.product}"

    def get_absolute_url(self):
        return reverse("store:cart_detail")