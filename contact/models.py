from django.db import models

# Create your models here.
class Contact(models.Model):
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
