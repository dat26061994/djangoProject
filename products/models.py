from django.db import models
from django.contrib.auth.models import User
from home.models import Category
from multiselectfield import MultiSelectField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator ,MaxValueValidator

# Create your models here.
class Product(models.Model):
    category =  models.ForeignKey(Category,related_name='cate_pr',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.FloatField()
    price_new = models.FloatField(default=1)
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

    # def get_price(self):
    #     return "{:,}".format(self.price)

class Product_Image(models.Model):
    product = models.OneToOneField(Product,related_name='product_image',on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='products/',default='products/image-none.png')
    image2 = models.ImageField(upload_to='products/',default='products/image-none.png')
    image3 = models.ImageField(upload_to='products/',default='products/image-none.png')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product.name
@receiver(post_save, sender=Product)
def create_product_image(sender, instance, created, **kwargs):
    if created:
        Product_Image.objects.create(product=instance)
post_save.connect(create_product_image,sender=Product)

class Product_Detail(models.Model):
    product_color = {
        ('Red', 'Red'),
        ('Black', 'Black'),
        ('Blue', 'Blue'),
        ('Grey', 'Grey'),
        ('Green', 'Green'),
        ('White', 'White'),
        ('Orange', 'Orange')
    }
    product_size = {
        ('XXL', 'XXL'),
        ('XL', 'XL'),
        ('L', 'L'),
        ('M', 'M'),
        ('S', 'S')
    }
    product = models.OneToOneField(Product,related_name='product_detail',on_delete=models.CASCADE)
    weight = models.FloatField(max_length=100,null=True,default='1')
    dimensions = models.CharField(max_length=100,null=True,default='1')
    materials = models.IntegerField(default='1')
    color = MultiSelectField(max_length=50,choices = product_color, default='Black')
    size = MultiSelectField(max_length=50,choices=product_size,default='L')

    def __str__(self):
        return self.product.name
def create_product_detail(sender, instance, created, **kwargs):
    if created:
        Product_Detail.objects.create(product=instance)
post_save.connect(create_product_detail,sender=Product)

class Review(models.Model):
    product =  models.ForeignKey(Product,related_name='product_review',on_delete=models.CASCADE)
    user =  models.ForeignKey(User,related_name='user_review',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    rating = models.FloatField(max_length=5,default=5)
    comments = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.NullBooleanField(default=True)

    def get_date(self):
        return self.created_at.strftime('%b %e %Y | %H:%M')

class Coupouns(models.Model):
    code = models.CharField(max_length=200,unique=True)
    discount = models.FloatField(max_length=100)
    valid_from = models.DateTimeField(null=True)
    valid_to = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status =  models.NullBooleanField(default=True)

    def __str__(self):
        return self.code
