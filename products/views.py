from django.shortcuts import render, get_object_or_404,HttpResponse
from .models import Product,Product_Image,Product_Detail
from home.models import Category
from django.conf import settings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def products(request):
    BASE_URL = settings.BASE_URL
    cats = Category.objects.all()
    if request.method == 'POST':
        if request.POST.get('search-product', False):
            prs = Product.objects.filter(name__contains = request.POST['search-product'])
        elif request.POST.get('price-pr', False):
            arr_price = request.POST.get('price-pr', False).split('-')
            prs = Product.objects.filter(price__gt=int(arr_price[0]),price__lt=int(arr_price[1]))
    else:
        prs = Product.objects.all();
    paginator  = Paginator(prs,3)
    page = request.GET.get('page')
    products_view = paginator.get_page(page)
    return render(request, 'products.html',{'cats':cats,'prs':products_view,'BASE_URL':BASE_URL})

def detail(request,pr_id):
    BASE_URL = settings.BASE_URL
    product = get_object_or_404(Product, pk=pr_id)
    product_img_detail = Product_Image.objects.get(product_id=pr_id)
    product_detail = Product_Detail.objects.get(product_id=pr_id)
    product_related = Product.objects.all()
    return render(request, 'product-detail.html',{'product_related':product_related,'prdetail':product,'primgdetail':product_img_detail,'prinfdetail':product_detail,'BASE_URL':BASE_URL})

def products_cat(request,pr_cat):
    BASE_URL = settings.BASE_URL
    cats = Category.objects.filter(pk=pr_cat)
    if request.method == 'POST':
        if request.POST.get('search-product', False):
            prs = Product.objects.filter(category_id=pr_cat,name__contains = request.POST['search-product'])
        elif request.POST.get('price-pr', False):
            arr_price = request.POST.get('price-pr', False).split('-')
            prs = Product.objects.filter(category_id=pr_cat,price__gt=int(arr_price[0]),price__lt=int(arr_price[1]))
    else:
        prs = Product.objects.filter(category_id=pr_cat)
    return render(request, 'products.html',{'cats':cats,'prs':prs,'BASE_URL':BASE_URL})
