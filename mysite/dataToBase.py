from products.models import Product
from home.models import Category,Gallery,Slider
from cart.cart import Cart
from django.conf import settings
from django.http import JsonResponse


def base(request):
    BASE_URL = settings.BASE_URL
    cates = Category.objects.all()
    cart = Cart(request)
    count_cart = cart.count()
    galleries = Gallery.objects.all()[:9]
    return {
        'cates':cates,
        'cart_base':cart,
        'BASE_URL':BASE_URL,
        'count_cart':count_cart,
        'galleries':galleries,
}
