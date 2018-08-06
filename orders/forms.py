from django import forms
from .models import Order
from django.contrib.auth.models import User


class OrderCreateForm(forms.ModelForm):
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
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(OrderCreateForm, self).form_valid(form)
    address = forms.CharField(label='Address',max_length=200,widget=forms.TextInput(attrs={'class': "form-control"}))
    phone = forms.CharField(label='Phone Number',max_length=20,widget=forms.TextInput(attrs={'class': "form-control"}))
    postal_code = forms.CharField(label='Postal Code',max_length=200,widget=forms.TextInput(attrs={'class': "form-control"}))

    class Meta:
        model = Order
        fields = ['user','first_name', 'last_name', 'email', 'address','phone', 'postal_code']
        exclude = ('user',)
