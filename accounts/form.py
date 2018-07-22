from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
import re
import datetime
from datetime import datetime

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
    phone = forms.CharField(label='Số điện thoại',max_length=20,widget=forms.TextInput(attrs={'class': "form-control"}))
    birth_day = forms.DateField(label='Ngày sinh',widget=forms.DateInput(attrs={'class': "form-control",'placeholder':'ngày/tháng/năm'}),input_formats=['%d/%m/%Y'],error_messages={
    'invalid': _('Sai ngày tháng năm (ngày/tháng/năm).'),
    },)
    # gender = forms.ChoiceField(widget=forms.Select(attrs={'class': "form-control"}))
    class Meta:
        model = UserProfile
        fields = ('address','phone','birth_day','gender')
        error_messages = {
            'address': {
                'max_length': _("Địa chỉ không được vượt quá 200 kí tự."),
            },
            'phone': {
                'max_length': _("Số điện thoại không được vượt quá 20 kí tự."),
            },
        }
    def clean_birth_day(self):
        birth_day = self.cleaned_data.get('birth_day')
        birth_day = datetime.strptime(str(birth_day), '%Y-%m-%d')
        if datetime.now() <= birth_day:
            raise forms.ValidationError(u'Wrong Date!')
        return birth_day

class SignupForm(UserCreationForm):
    username = forms.RegexField(regex=r'^[\w.@+-]+$',label="Tên đăng nhập",max_length=200,
    widget=forms.TextInput(attrs={'class':'form-control'}),
    error_messages={'invalid':'Tên đăng nhập không được chứa kí tự đặc biệt!'}
    )
    email = forms.EmailField(label="Email",max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="Mật khẩu",max_length=200,widget=forms.PasswordInput(attrs={'class':'form-control'}),
    error_messages={'required':'Mật khẩu không được bỏ trống!'}
    )
    password2 = forms.CharField(label="Xác nhận mật khẩu",max_length=200,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
    def clean_username(self):
        username = self.cleaned_data['username']
        existing = User.objects.filter(username__iexact=self.cleaned_data['username'])
        if existing.exists():
            raise forms.ValidationError(_("Tên đăng nhập đã có người sử dụng"))
        elif not re.search(r'^\w+$', username):
            raise forms.ValidationError("Tên đăng nhập chỉ có thể chứa")
        else:
            return self.cleaned_data['username']

    def clean_email(self):
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_("Email đã có người sử dụng. Vui lòng chọn email khác!"))
        return self.cleaned_data['email']

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise forms.ValidationError(_("Mật khẩu không trùng khớp!"))

class changeAvatarForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('avatar',)
    # def clean(self):
    #     cleaned_data = super(SignupForm, self).clean()
    #     username = cleaned_data.get("username")
    #     email = cleaned_data.get("email")
    #     password1 = cleaned_data.get("password1")
    #     password2 = cleaned_data.get("password2")
    #     existing = User.objects.filter(username__iexact=self.cleaned_data['username'])
    #     if existing.exists():
    #         raise forms.ValidationError(_("Tên đăng nhập đã có người sử dụng"))
    #     elif not re.search(r'^\w+$', username):
    #         raise forms.ValidationError("Tên đăng nhập chỉ có thể chứa")
    #
    #     if User.objects.filter(email__iexact=self.cleaned_data['email']):
    #         raise forms.ValidationError(_("Email đã có người sử dụng. Vui lòng chọn email khác!"))
    #     if password1 != password2:
    #         raise forms.ValidationError(_("Mật khẩu không trùng khớp!"))
    #     return self.cleaned_data
