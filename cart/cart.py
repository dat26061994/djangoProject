from decimal import Decimal
from django.conf import settings
from products.models import Product,Coupouns
import json



class Cart(object):
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        self.coupon_id = self.session.get('coupon_id')
    def add(self,product,quantity=1,color='Black',size='L'):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0,'price':str(product.price),'color':color,'size':size}
            self.cart[product_id]['quantity'] = quantity
        else:
            tem = self.cart[product_id]['quantity']
            quan = int(tem)
            quan += int(quantity)
            self.cart[product_id]['quantity']  = quan
            self.cart[product_id]['color'] = color
            self.cart[product_id]['size'] = size
        self.save()

    def update(self,product,quantity=1,color='Black',size='L',update_quantity=False):
        product_id = str(product.id)
        self.cart[product_id]['quantity'] = quantity
        self.cart[product_id]['color'] = color
        self.cart[product_id]['size'] = size
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self,product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids).values('id','name','price','image')
        for product in products:
            self.cart[str(product['id'])]['product'] = product
        for item in self.cart.values():
            item['price'] = float("{0:.2f}".format(float(item['price'])))
            item['total_price'] = float("{0:.2f}".format(item['price'] * int(item['quantity'])))
            yield item
    def count(self):
        return len(self.cart.values())

    def __len__(self):
        return sum(int(item['quantity']) for item in self.cart.values())

    def get_total_price(self):
        total = float("{0:.2f}".format(sum(float(item['price']) * int(item['quantity']) for item in self.cart.values())))
        return total
    @property
    def coupon(self):
        if self.coupon_id:
            try:
                coupon = Coupouns.objects.get(id=self.coupon_id,status=True)
            except Coupouns.DoesNotExist:
                return None
            return coupon
        return None
    def get_discount(self):
        if self.coupon:
            return float((self.coupon.discount / 100) * self.get_total_price())
        return 0
    def get_total_price_after_discount(self):
        return self.get_total_price() - self.get_discount()
    def get_total(self):
        total =  float("{0:.2f}".format(sum(float(item['price']) * int(item['quantity']) for item in self.cart.values())))
        if total > 600:
            total = total
        else:
            total = total + 30
        if self.coupon:
            discount = float((self.coupon.discount / 100) * self.get_total_price())
        else:
            discount = 0
        return total - discount

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
