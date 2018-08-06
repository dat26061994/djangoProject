from django.shortcuts import render
from .models import About
from django.conf import settings


# Create your views here.
def about(request):
    BASE_URL = settings.BASE_URL
    try:
        ab1 = About.objects.get(column='column 1')
        ab2 = About.objects.get(column='column 2')
    except About.DoesNotExist:
        return None
    return render(request,'about.html',{'ab1':ab1,'ab2':ab2,'BASE_URL':BASE_URL})
