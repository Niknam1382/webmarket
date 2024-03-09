from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class color(models.Model):
    color = models.CharField(max_length=255)
    def __str__(self):
        return self.color
    
class size(models.Model):
    size = models.CharField(max_length=255)
    def __str__(self):
        return self.size
    
class brand(models.Model):
    brand = models.CharField(max_length=255)
    def __str__(self):
        return self.brand

class product(models.Model):
    image = models.ImageField(upload_to='store')
    image2 = models.ImageField(upload_to='store', null=True, blank=True)
    image3 = models.ImageField(upload_to='store', null=True, blank=True)
    name = models.CharField(max_length=255)
    available = models.BooleanField(default=0)
    price = models.IntegerField()
    price_off = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    questions = models.TextField(null=True, blank=True)     # new item added
    category = models.ManyToManyField(Category)
    tags = TaggableManager()
    color = models.ForeignKey(color, on_delete=models.SET_NULL, null=True, blank=True)
    size = models.ForeignKey(size, on_delete=models.SET_NULL, null=True, blank=True) 
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    star = models.IntegerField(null=True, blank=True)
    star_c = models.IntegerField(default=0)
    star_t = models.IntegerField(default=0)
    brand = models.ForeignKey(brand, on_delete=models.CASCADE, null=True, blank=True)
    inventory = models.PositiveIntegerField(null=True, blank=True)

class Cart_Detail2(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    email = models.EmailField()
    city = models.CharField(max_length=255)
    address1 = models.TextField()
    address2 = models.TextField(null=True, blank=True)
    code_posti = models.IntegerField()

class StoreComment(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    message = models.TextField()
    star = models.IntegerField(null=True, blank=True)
    approved = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.first_name+' '+self.last_name