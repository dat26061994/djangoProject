from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_http_methods,require_POST
from products.models import Product,Coupouns
from .cart import Cart
from .forms import CartAddProductForm,CouponApplyForm
from django.conf import settings
from django.http import JsonResponse,HttpResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.template.loader import render_to_string
from django.core import serializers
from django.utils import timezone

# Create your views here.
BASE_URL = settings.BASE_URL
@require_POST
def cart_add(request,product_id):
    cart = Cart(request)
    try:
        product = get_object_or_404(Product,id=product_id)
    except Product.DoesNotExist:
        return None
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        quantity = int(cd['quantity'])
        cart.add(product=product,quantity=quantity,color=cd['color'],size=cd['size'])
    return redirect('cart:cart_detail')

def cart_update(request,product_id):
    cart = Cart(request)
    try:
        product = get_object_or_404(Product,id=product_id)
    except Product.DoesNotExist:
        return None
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        quantity = int(cd['quantity'])
        cart.update(product=product,quantity=quantity,color=cd['color'],size=cd['size'])
    return redirect('cart:cart_detail')
@require_POST
def coupon_apply(request):
    data = dict()
    cart = Cart(request)
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupouns.objects.get(code__iexact=code,
                                        valid_from__lte=now,
                                        valid_to__gte=now,
                                        status=True)
            request.session['coupon_id'] = coupon.id
        except Coupouns.DoesNotExist:
            request.session['coupon_id'] = None
    return redirect('cart:cart_detail')

def cart_addajax(request,product_id):
    BASE_URL = settings.BASE_URL
    data = dict()
    cart = Cart(request)
    try:
        product = get_object_or_404(Product,id=product_id)
    except Product.DoesNotExist:
        return None
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        quantity = int(cd['quantity'])
        cart.add(product=product,quantity=quantity,color=cd['color'],size=cd['size'])
        data['success'] = True
        data['message'] = "Added to Cart"
        data['count'] = cart.count()
        data['cart'] = render_to_string('pages/cartBase.html',{'BASE_URL':BASE_URL,'cart_base':cart})
        return JsonResponse(data)
    else:
        data['success'] = False
        data['message'] = 'Please try agian!!'
        return JsonResponse(data)


def cart_remove(request,product_id):
    cart = Cart(request)
    try:
        product = get_object_or_404(Product,id=product_id)
    except Product.DoesNotExist:
        return None
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],'color':item['color'],'size':item['size']})
    coupon_apply_form = CouponApplyForm()
    return render(request,'detail.html',{'cart':cart,'coupon_apply_form':coupon_apply_form,'BASE_URL':BASE_URL})
