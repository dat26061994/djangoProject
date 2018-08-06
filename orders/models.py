from django.db import models
from django.contrib.auth.models import User
from products.models import Product,Coupouns


# Create your models here.

class Order(models.Model):
    user =  models.ForeignKey(User,related_name='user_orders',on_delete=models.CASCADE)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=150,default='1')
    postal_code = models.CharField(max_length=30)
    shiped_date =  models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    status = models.NullBooleanField(default=True)
    coupon = models.ForeignKey(Coupouns, related_name='coupon', on_delete=models.CASCADE,null=True,blank=True)
    discount = models.IntegerField(default=0,max_length=200)
    total = models.FloatField(default=0,max_length=200)


    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return float(total_cost) - (float(total_cost) * (self.discount/100))

    def get_datecreated(self):
        return self.created.strftime('%b %e %Y')

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    discount = models.IntegerField(default=0)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
