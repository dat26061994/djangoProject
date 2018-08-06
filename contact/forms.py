from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={
    'class':'form-control stext-111 cl2 plh3 size-116 p-l-62 p-r-30',
    'placeholder':'Your Email',
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
    'class':'form-control stext-111 cl2 plh3 size-120 p-lr-28 p-tb-25',
    'placeholder':'How Can We Help?',
    }), required=True)
