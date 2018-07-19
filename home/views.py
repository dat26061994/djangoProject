from django.shortcuts import render
from .models import Slider,Category,Gallery
from products.models import Product,Product_Image,Product_Detail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_list_or_404, get_object_or_404,HttpResponse
import json
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings

# Create your views here.
def home(request):
    BASE_URL = settings.BASE_URL
    slides = Slider.objects.all()[:3]
    cats = Category.objects.all()
    products = Product.objects.order_by('created_at')
    galleries = Gallery.objects.all()[:9]
    paginator  = Paginator(products,3)
    page = request.GET.get('page')
    products_view = paginator.get_page(page)
    return render(request, 'pages/home.html',{'slides':slides,'cats':cats,'products':products_view,'galleries':galleries,'BASE_URL':BASE_URL})

def product_detail(request,product_id):
    product = Product.objects.values('id','name','description','price','quantity','image').get(id=product_id)
    images = Product_Image.objects.all().filter(product_id=product_id).values('image1','image2','image3')
    product_detail = Product_Detail.objects.all().filter(product_id=product_id).values('color','size')
    return JsonResponse({'product':product,'product_image':list(images),'product_detail':list(product_detail)})
