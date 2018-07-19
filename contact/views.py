from django.shortcuts import render
from .models import Contact
from django.conf import settings

# Create your views here.

def contact(request):
    BASE_URL = settings.BASE_URL
    contact = Contact.objects.first()
    return render(request,'contact.html',{'contact':contact,'BASE_URL':BASE_URL})
