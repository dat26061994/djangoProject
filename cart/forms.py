from django import forms
from products.models import Coupouns

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,21)]
product_color = {
    ('Red', 'Red'),
    ('Black', 'Black'),
    ('Blue', 'Blue'),
    ('Grey', 'Grey'),
    ('Green', 'Green'),
    ('White', 'White'),
    ('Orange', 'Orange')
}
product_size = {
    ('XXL', 'XXL'),
    ('XL', 'XL'),
    ('L', 'L'),
    ('M', 'M'),
    ('S', 'S')
}

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(label='Quantity',max_value=100,min_value=0,widget=forms.NumberInput(attrs={'name':'num-product','value':'1','class': "form-control mtext-104 cl3 txt-center",'min':'0','max':'100'}))
    color = forms.ChoiceField(choices=product_color,initial='',label="Color",widget=forms.Select(attrs={
    'class':'form-control',
    'name':'color-product'
    }),)
    size = forms.ChoiceField(choices=product_size,initial='',label="Size",widget=forms.Select(attrs={
    'class':'form-control',
    'name':'color-product'
    }),)
    # update = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)

class CouponApplyForm(forms.Form):
    code = forms.CharField(label='Coupon',widget=forms.TextInput(attrs={'class':'form-control'}))
