from django import forms
from .models import Review
from django.contrib.auth.models import User

class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields={'comments','name','email'}
