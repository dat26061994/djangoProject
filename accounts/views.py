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
from .form import SignupForm,changeAvatarForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate
import datetime

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
            messages.error(request,'Tên đăng nhập hoặc mật khẩu không chính xác!')
            return render(request, 'login.html',{'BASE_URL':BASE_URL})
    else:
        return render(request, 'login.html',{'BASE_URL':BASE_URL})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

@login_required(login_url="login")
def userProfile(request):
    userprofile = UserProfile.objects.get(user=request.user)
    if request.method =="POST":
        form = changeAvatarForm(request.POST,request.FILES,instance=userprofile)
        if form.is_valid():
            messages.success(request,'Ảnh đại diện đã được thay đổi!')
            form.save()
    else:
        form = changeAvatarForm()
    return render(request,'profile.html',{'BASE_URL':BASE_URL,'userprofile':userprofile,'form':form})

def editProfile(request):
    userprofile = UserProfile.objects.get(user=request.user)
    
    if request.method =="POST":
        userForm = UserForm(request.POST,instance=request.user)
        profileForm = ProfileForm(request.POST,instance=userprofile)
        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            profileForm.save()
            messages.success(request,'Thông tin tài khoản đã được cập nhật!')
            return redirect('userProfile')
        else:
            pass
    else:
        userForm = UserForm(instance=request.user)
        profileForm = ProfileForm(instance=userprofile)
    return render(request,'editProfile.html',{'BASE_URL':BASE_URL,'userForm':userForm,'profileForm':profileForm,'userprofile':userprofile})
def editAvatar(request):
    pass
def changePassword(request):
    old_password = User.objects.filter(id=request.user.id).values('password')[0]['password']
    if request.method == "POST":
        if not request.user.check_password(request.POST['old_password']):
            messages.error(request,'Mật khẩu cũ không chính xác!')
        else:
            if 8 < len(request.POST['new_password']) < 200 and not request.POST['new_password'].isdigit():
                if request.POST['new_password'] == request.POST['re_new_password']:
                    u = User.objects.get(pk=request.user.id)
                    u.set_password(request.POST['re_new_password'])
                    u.save()
                    messages.success(request,'Mật khẩu đã được thay đổi!')
                    return redirect('userProfile')
                else:
                    messages.error(request,'Mật khẩu mới không trùng khớp!')
            else:
                if len(request.POST['new_password']) < 8 or len(request.POST['new_password']) > 200:
                    messages.error(request,'Mật khẩu phải từ 8 đến 200 ký tự!')
                elif request.POST['new_password'].isdigit():
                    messages.error(request,'Mật khẩu phải chứa ít nhất 1 ký tự!')

    return render(request,'changePassword.html',{'BASE_URL':BASE_URL})
