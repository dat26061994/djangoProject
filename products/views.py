from django.shortcuts import render, get_object_or_404,HttpResponse
from .models import Product,Product_Image,Product_Detail,Review
from accounts.models import UserProfile
from home.models import Category
from django.conf import settings
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from cart.forms import CartAddProductForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import ReviewCreateForm
import re
from django.contrib.auth.models import User
from django.db.models import Count
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



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
    paginator  = Paginator(prs,20)
    page = request.GET.get('page')
    products_view = paginator.get_page(page)
    return render(request, 'products.html',{'cats':cats,'prs':products_view,'BASE_URL':BASE_URL})

def detail(request,pr_id):
    data = dict()
    BASE_URL = settings.BASE_URL
    try:
        product = get_object_or_404(Product, pk=pr_id)
    except Product.DoesNotExist:
        return None
    try:
        r = Review.objects.select_related('user','user__user_profile').filter(product_id=pr_id).order_by('-created_at')
    except Review.DoesNotExist:
        return None
    paginator  = Paginator(r,5)
    page = request.GET.get('page')
    reviews = paginator.get_page(page)
    if request.is_ajax():
        data['review'] = render_to_string('review.html',{'BASE_URL':BASE_URL,'review':reviews})
        data['page'] = reviews.number
        data['totalpage'] = len(reviews.paginator.page_range)
        return JsonResponse(data)
    else:
        product_img_detail = Product_Image.objects.get(product_id=pr_id)
        product_detail = Product_Detail.objects.get(product_id=pr_id)
        product_related = Product.objects.all()
        cart_product_form = CartAddProductForm()
        return render(request, 'product-detail.html',{'r':r,'review':reviews,'cart_product_form':cart_product_form,'product_related':product_related,'prdetail':product,'primgdetail':product_img_detail,'prinfdetail':product_detail,'BASE_URL':BASE_URL})

def products_cat(request,pr_cat):
    BASE_URL = settings.BASE_URL
    try:
        cats = Category.objects.filter(pk=pr_cat)
    except Category.DoesNotExist:
        return None
    if request.method == 'POST':
        if request.POST.get('search-product', False):
            prs = Product.objects.filter(category_id=pr_cat,name__contains = request.POST['search-product'])
        elif request.POST.get('price-pr', False):
            arr_price = request.POST.get('price-pr', False).split('-')
            prs = Product.objects.filter(category_id=pr_cat,price__gt=int(arr_price[0]),price__lt=int(arr_price[1]))
    else:
        prs = Product.objects.filter(category_id=pr_cat)
    return render(request, 'products.html',{'cats':cats,'prs':prs,'BASE_URL':BASE_URL})

def review(request,pr_id):
    BASE_URL = settings.BASE_URL
    data = dict()
    form = ReviewCreateForm()
    valid = True

    if request.method == 'POST':
        list_dirty_word = ('địt','lồn','đụ')

        product = Product.objects.get(id=pr_id)
        u = User.objects.get(id=1)
        comments = request.POST['comments']
        rating = request.POST['rating']
        if request.user.is_authenticated:
            user = request.user
            if request.user.get_full_name():
                name = request.user.get_full_name()
            else:
                name = "Anomous"
            email = request.user.email
        else:
            user = u
            name = request.POST['name']
            email = request.POST['email']
        if not name or not email or not comments:
            valid = False
        elif len(name)>200:
            valid = True
        if email:
            if not EMAIL_REGEX.match(email):
                valid = False
            elif len(email) >200:
                valid = False
        if valid:
            re = Review(product=product,user=user,name=name,email=email,comments=comments,rating=rating)
            re.save()
            r = Review.objects.select_related('user','user__user_profile').filter(product_id=pr_id).order_by('-created_at')
            paginator  = Paginator(r,5)
            page = request.GET.get('page')
            reviews = paginator.get_page(page)
            data['review'] = render_to_string('review.html',{'r':r,'review':reviews,'BASE_URL':BASE_URL})
            data['count'] = len(r)
            data['success'] = True
        else:
            data['review'] = render_to_string('review.html')
    return JsonResponse(data)
