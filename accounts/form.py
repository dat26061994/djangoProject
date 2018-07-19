from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

# from .validators import clean_email

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserForm(forms.ModelForm):
    first_name = forms.CharField(label='Họ',max_length=200,widget=forms.TextInput(attrs={'class': "form-control",'lable':'first_name'}))
    last_name = forms.CharField(label='Tên',max_length=200,widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(
    label='Email',
    required=True,
    max_length=200,
    widget=forms.TextInput(attrs={'class': "form-control",'type':'email'}),
    error_messages={
    'required': 'Email không được để trống!',
    'max_length':'Email vượt quá 200 kí tự',
    }
    )
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and not EMAIL_REGEX.match(email):
            raise ValidationError("Email không đúng định dạng.")
        elif User.objects.filter(email=email).exclude(pk=self.instance.id):
            raise ValidationError("Email đã tồn tại.")
        return email

class ProfileForm(forms.ModelForm):
    # avatar = forms.FileField(widget=forms.FileInput(attrs={'class': "form-control"}))
    address = forms.CharField(label='Địa chỉ',max_length=200,widget=forms.TextInput(attrs={'class': "form-control"}))
    phone = forms.CharField(label='Số điện thoại',max_length=200,widget=forms.TextInput(attrs={'class': "form-control"}))
    birth_day = forms.DateField(label='Ngày sinh',widget=forms.TextInput(attrs={'class': "form-control"}))
    # gender = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}))
    class Meta:
        model = UserProfile
        fields = ('address','phone','birth_day','gender')
