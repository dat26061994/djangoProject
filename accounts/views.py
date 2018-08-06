from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse,HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
import re
from .form import UserForm,ProfileForm
from .models import UserProfile
from datetime import datetime, date, time
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm,UserCreationForm
from .form import SignupForm,changeAvatarForm,changePasswordForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate
import datetime
from orders.models import Order,OrderItem
from products.models import Product
from wishlist.models import WishList
from django.http import JsonResponse,HttpResponse
from django.template.loader import render_to_string

# Create your views here.
BASE_URL = settings.BASE_URL
def signup(request):
    BASE_URL = settings.BASE_URL
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            raw_password = request.POST['password1']
            user = auth.authenticate(username=request.POST['username'],password=request.POST['password1'])
            auth.login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'signup.html',{'BASE_URL':BASE_URL,'form':form})


def login(request):
    BASE_URL = settings.BASE_URL
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request,'Your username and password did not match. Please try again.')
            return render(request, 'login.html',{'BASE_URL':BASE_URL})
    else:
        return render(request, 'login.html',{'BASE_URL':BASE_URL})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

@login_required(login_url="login")
def userProfile(request):
    try:
        userprofile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        return None
    if request.method =="POST":
        form = changeAvatarForm(request.POST,request.FILES,instance=userprofile)
        if form.is_valid():
            messages.success(request,'Avatar was change!')
            form.save()
    else:
        form = changeAvatarForm()
    return render(request,'profile.html',{'BASE_URL':BASE_URL,'userprofile':userprofile,'form':form})
@login_required(login_url="login")
def editProfile(request):
    try:
        userprofile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        return None
    if request.method =="POST":
        userForm = UserForm(request.POST,instance=request.user)
        profileForm = ProfileForm(request.POST,instance=userprofile)
        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            profileForm.save()
            messages.success(request,'Update is success!')
            return redirect('userProfile')
        else:
            pass
    else:
        userForm = UserForm(instance=request.user)
        profileForm = ProfileForm(instance=userprofile)
    return render(request,'editProfile.html',{'BASE_URL':BASE_URL,'userForm':userForm,'profileForm':profileForm,'userprofile':userprofile})
@login_required(login_url="login")

def editAvatar(request):
    pass

@login_required(login_url="login")
def changePassword(request):
    old_password = User.objects.filter(id=request.user.id).values('password')[0]['password']
    if request.method == "POST":
        form = changePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please try again.')
    else:
        form = changePasswordForm(request.user)

    return render(request,'changePassword.html',{'BASE_URL':BASE_URL,'form':form})


@login_required(login_url="login")
def ordersInfor(request):
    data = dict()
    try:
        orders = Order.objects.filter(user=request.user)
    except Order.DoesNotExist:
        return None
    try:
        orderItems = OrderItem.objects.select_related('order').select_related('product').filter(order__in=orders)
    except OrderItem.DoesNotExist:
        return None
    return render(request,'orders.html',{'BASE_URL':BASE_URL,'orders':orders,'orderItems':orderItems})

@login_required(login_url="login")
def orderDetail(request,order_id):
    try:
        orderItems = OrderItem.objects.select_related('order').select_related('product').filter(order_id=order_id)
    except OrderItem.DoesNotExist:
        return None
    return render(request,'orderDetail.html',{'BASE_URL':BASE_URL,'orders':orderItems})
@login_required(login_url="login")
def wishlist(request):
    try:
        wishlist = WishList.objects.select_related('product').filter(user=request.user)
    except WishList.DoesNotExist:
        return None
    return render(request,'wishlist.html',{'BASE_URL':BASE_URL,'wishlist':wishlist})
@login_required(login_url="login")
def addWishlist(request):
    product_id = request.POST["product_id"]
    if not WishList.objects.filter(product_id=product_id,user=request.user).exists():
        w = WishList(user=request.user,product_id=product_id)
        w.save()
        return JsonResponse({"success": True,"message":"Added to wishlist"})
    else:
        return JsonResponse({"success": False, "message": "Product is exists in wishlist"})
@login_required(login_url="login")
def delwishlist(request,id):
    data = dict()
    try:
        delwishlist = WishList.objects.get(pk=id)
    except WishList.DoesNotExist:
        return None
    if request.method == "POST":
        delwishlist.delete()
        wishlist = WishList.objects.select_related('product').filter(user=request.user)
        data['wishlist'] = render_to_string('wishlist2.html',{'wishlist':wishlist})
        data['success'] = True
    else:
        context = {'delwishlist':delwishlist}
        data['html_form'] = render_to_string('delWishlist.html',context,request=request)
    return JsonResponse(data)
