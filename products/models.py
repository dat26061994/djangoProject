from django.db import models
from django.contrib.auth.models import User
from home.models import Category
from multiselectfield import MultiSelectField

# Create your models here.
class Product(models.Model):
    category =  models.ForeignKey(Category,related_name='cate_pr',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.IntegerField()
    price_new = models.IntegerField(default=1)
    quantity = models.IntegerField(default=1)
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    status = models.NullBooleanField(default=True)
    order = models.IntegerField(default=1)
    tags = models.CharField(null=True,default='Tags',max_length=200)

    def __str__(self):
        return self.name

    def get_date(self):
        return self.created_at.strftime('%b %e %Y')

    def get_price(self):
        return "{:,}".format(self.price)

class Product_Image(models.Model):
    product = models.ForeignKey(Product,related_name='product_image',on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/')
    image3 = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

class Product_Detail(models.Model):
    product_color = {
        ('Red', 'Đỏ'),
        ('Black', 'Đen'),
        ('Blue', 'Xanh da trời'),
        ('Grey', 'Xám'),
        ('Green', 'Xanh nước biển'),
        ('White', 'Trắng'),
        ('Orange', 'Da cam')
    }
    product_size = {
        ('XXL', 'XXL'),
        ('XL', 'XL'),
        ('L', 'L'),
        ('M', 'M'),
        ('S', 'S')
    }
    product = models.ForeignKey(Product,related_name='product_detail',on_delete=models.CASCADE)
    weight = models.FloatField(max_length=100)
    dimensions = models.CharField(max_length=100)
    materials = models.IntegerField()
    color = MultiSelectField(max_length=50,choices = product_color, default='Black')
    size = MultiSelectField(max_length=50,choices=product_size,default='L')
