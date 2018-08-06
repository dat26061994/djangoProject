from django.shortcuts import render
from .models import Slider,Category,Gallery
from products.models import Product,Product_Image,Product_Detail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_list_or_404, get_object_or_404,HttpResponse
import json
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from django.template.loader import render_to_string
from cart.forms import CartAddProductForm
from django.http import Http404


# Create your views here.
def home(request):
    BASE_URL = settings.BASE_URL
    slides = Slider.objects.all()[:3]
    cats = Category.objects.all()
    products = Product.objects.order_by('created_at')
    galleries = Gallery.objects.all()[:9]
    paginator  = Paginator(products,12)
    page = request.GET.get('page')
    products_view = paginator.get_page(page)
    return render(request, 'pages/home.html',{'slides':slides,'cats':cats,'products':products_view,'galleries':galleries,'BASE_URL':BASE_URL})

def product_detail(request,product_id):
    data = dict()
    try:
        product = Product.objects.values('id','name','description','price','quantity','image').get(id=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    try:
        images = Product_Image.objects.values('image1','image2','image3').get(product_id=product_id)
    except Product_Image.DoesNotExist:
        raise Http404("Product Image does not exist")
    try:
        product_detail = Product_Detail.objects.values('color','size').get(product_id=product_id)
    except Product_Detail.DoesNotExist:
        raise Http404("product_detail does not exist")
    cart_add_form = CartAddProductForm()
    data['product'] = product
    data['images'] = images
    data['product_detail'] = product_detail
    data['html'] = render_to_string('pages/prDetail.html',{'product':product,'images':images,'product_detail':product_detail,'cart_add_form':cart_add_form},request=request)
    return JsonResponse(data)
