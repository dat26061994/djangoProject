from django.db import models
from django.contrib.auth.models import User
from products.models import Product
# Create your models here.
class WishList(models.Model):
    user =  models.ForeignKey(User,related_name='wishlist_user',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='wishlist_pr',on_delete=models.CASCADE)
    
