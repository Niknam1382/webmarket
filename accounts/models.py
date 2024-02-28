from django.db import models
from store.models import product
from django.contrib.auth.models import User
from django.urls import reverse

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    is_paid = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.product}"

    def get_absolute_url(self):
        return reverse("store:cart_detail")

class RegisteredCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    email = models.EmailField()
    city = models.CharField(max_length=255)
    address1 = models.TextField()
    address2 = models.TextField(null=True, blank=True)
    code_posti = models.IntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='profile', default='images/default.jpg')

    def __str__(self):
        return self.user.username