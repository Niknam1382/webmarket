from django.db import models
from django.contrib.auth.models import User
from jdatetime import date
from persian_tools import digits

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Post(models.Model) :
    image = models.ImageField(upload_to='blog', default='blog/default.jpg')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.title, self.id)
    
    def shamsi_publish_date(self):
           return date.fromgregorian(date=self.published_at)
    
    class Meta:
        ordering = ('created_at',)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.first_name+' '+self.last_name