from django.db import models
from taggit.managers import TaggableManager

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


class product(models.Model):
    image = models.ImageField(upload_to='store', default='store/default.jpg')
    name = models.CharField(max_length=255)
    available = models.BooleanField(default=0)
    price = models.IntegerField()
    description = models.TextField()
    category = models.ManyToManyField(Category)
    tags = TaggableManager()
    color = models.ManyToManyField(color)
    size = models.ManyToManyField(size)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)