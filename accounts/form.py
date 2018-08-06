from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.utils.translation import ugettext_lazy as _
import re
import datetime
from datetime import datetime

# from .validators import clean_email

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name',max_length=200,widget=forms.TextInput(attrs={'class': "form-control",'lable':'first_name'}))
    last_name = forms.CharField(label='Last Name',max_length=200,widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(
    label='Email',
    required=True,
    max_length=200,
    widget=forms.TextInput(attrs={'class': "form-control",'type':'email'}),
    error_messages={
    'required': 'Email is required!',
    }
    )
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and not EMAIL_REGEX.match(email):
            raise ValidationError("Email is not valid.")
        elif User.objects.filter(email=email).exclude(pk=self.instance.id):
            raise ValidationError("Email is exists!.")
        return email

class ProfileForm(forms.ModelForm):
    # avatar = forms.FileField(widget=forms.FileInput(attrs={'class': "form-control"}))
    address = forms.CharField(label='Address',max_length=200,widget=forms.TextInput(attrs={'class': "form-control"}))
    phone = forms.CharField(label='Phone Number',max_length=20,widget=forms.TextInput(attrs={'class': "form-control"}))
    birth_day = forms.DateField(label='Birth Day',widget=forms.DateInput(attrs={'class': "form-control",'placeholder':'Y-m-d'}),)
    # gender = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}))
    class Meta:
        model = UserProfile
        fields = ('address','phone','birth_day','gender')
        error_messages = {
            'address': {
                'max_length': _("Address maximum 200 digits."),
            },
            'phone': {
                'max_length': _("Phone number maximum 20 digits."),
            },
        }
    def clean_birth_day(self):
        birth_day = self.cleaned_data.get('birth_day')
        birth_day = datetime.strptime(str(birth_day), '%Y-%m-%d')
        if datetime.now() <= birth_day:
            raise forms.ValidationError(u'Wrong Date!')
        return birth_day

class SignupForm(UserCreationForm):
    username = forms.RegexField(regex=r'^[\w.@+-]+$',label="Username",max_length=200,
    widget=forms.TextInput(attrs={'class':'form-control'}),
    error_messages={'invalid':'Username can not contain special characters '}
    )
    email = forms.EmailField(label="Email",max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="Mật khẩu",max_length=200,widget=forms.PasswordInput(attrs={'class':'form-control'}),
    error_messages={'required':'Password is not empty!'}
    )
    password2 = forms.CharField(label="Xác nhận mật khẩu",max_length=200,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     existing = User.objects.filter(username__iexact=self.cleaned_data['username'])
    #     if existing.exists():
    #         raise forms.ValidationError(_("Username is exits"))
    #     elif not re.search(r'^\w+$', username):
    #         raise forms.ValidationError("Tên đăng nhập chỉ có thể chứa")
    #     else:
    #         return self.cleaned_data['username']
    #
    # def clean_username(self):
    #     if len(self.cleaned_data['username']) < 6 or len(self.cleaned_data['username'])<20:
    #         raise forms.ValidationError(_("Username is invalid(6 - 20 digits)"))
    def clean_email(self):
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_("Email is exists.Please choose other email!"))
        return self.cleaned_data['email']
    #
    # def clean_password2(self):
    #     if self.cleaned_data['password1'] != self.cleaned_data['password2']:
    #         raise forms.ValidationError(_("Mật khẩu không trùng khớp!"))

class changeAvatarForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('avatar',)

class changePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(required=True, label='Old Password',
                      widget=forms.PasswordInput(attrs={
                        'class': 'form-control'}),
                      error_messages={
                        'required': 'Old password is required'})
    new_password1 = forms.CharField(required=True, label='New password',
                      widget=forms.PasswordInput(attrs={
                        'class': 'form-control'}),
                      error_messages={
                        'required': 'New password is required'})
    new_password2 = forms.CharField(required=True, label='Confirm new password',
                      widget=forms.PasswordInput(attrs={
                        'class': 'form-control'}),
                      error_messages={
                        'required': 'The field is required'})

    class Meta:
        model = User
        fields = ( 'old_password', 'new_password1', 'new_password2', )
