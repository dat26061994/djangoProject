from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re
from .validators import clean_email

EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(
    validators=[clean_email],
    required=True,
    max_length=200,
    widget=forms.TextInput(attrs={'class': "form-control",'type':'email'}),
    error_messages={'required': 'Email không được để trống!'}
    )
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    # avatar = forms.FileField(widget=forms.FileInput(attrs={'class': "form-control"}))
    address = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': "form-control"}))
    phone = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': "form-control"}))
    birth_day = forms.DateField(widget=forms.TextInput(attrs={'class': "form-control"}))
    # gender = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}))
    class Meta:
        model = UserProfile
        fields = ('address','phone','birth_day','gender')
