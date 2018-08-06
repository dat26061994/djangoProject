from django.shortcuts import render,redirect
from .models import Contact
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm
from django.contrib import messages
# Create your views here.

def contact(request):
    BASE_URL = settings.BASE_URL
    contact = Contact.objects.first()
    form = ContactForm()
    return render(request,'contact.html',{'contact':contact,'form':form,'BASE_URL':BASE_URL})

def send(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Thank you for contact"
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, [settings.EMAIL_HOST_USER,from_email],fail_silently=False,)
                messages.success(request, 'Thank you for your message.')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        return redirect('contact')
