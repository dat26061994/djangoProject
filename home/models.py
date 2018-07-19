from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Slider(models.Model):
    name = models.CharField(max_length=100)
    title = models.TextField(max_length=200)
    image = models.ImageField(upload_to='slides/')
    b_image = models.ImageField(upload_to='slides/')
    Link = models.TextField(max_length=200,null=True)
    Description = models.TextField(max_length=200,null=True)
    Created_At = models.DateTimeField(auto_now_add=True)
    Created_By = models.ForeignKey(User,related_name='user_name_cre',on_delete=models.CASCADE)
    Modified_At = models.DateTimeField(auto_now_add=True)
    Modified_By = models.ForeignKey(User,related_name='user_name_update',on_delete=models.CASCADE)
    Status = models.NullBooleanField(default=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    title = models.TextField(max_length=200)
    image = models.ImageField(upload_to='categories/')
    status = models.NullBooleanField(default=True)
    Created_At = models.DateTimeField(auto_now_add=True)
    Modified_At = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    status = models.NullBooleanField(default=True)
    Created_At = models.DateTimeField(auto_now_add=True)
    Modified_At = models.DateTimeField(auto_now_add=True)
    
