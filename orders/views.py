from django.shortcuts import render,redirect
from django.urls import reverse
from .models import OrderItem,Order
from accounts.models import UserProfile
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.auth.models import User
from products.models import Product,Coupouns
from django.core.mail import send_mail
from django.conf import settings


def order_create(request):
    cart = Cart(request)
    u = User.objects.get(id=1)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            else:
                order.user = u
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
                coupouns = Coupouns.objects.get(code=cart.coupon)
                coupouns.status = False
                coupouns.save()
            order.total = request.POST.get('total', False)
            order.save()
            for item in cart:
                product = Product.objects.filter(id=item['product']['id'])
                OrderItem.objects.create(
                    order=order,
                    product_id=item['product']['id'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            subject = "Thank you for your order"
            message = "Success to order"
            from_email = settings.EMAIL_HOST_USER
            to_email = list(form.cleaned_data['email'])
            send_mail(
                        subject,
                        message,
                        settings.EMAIL_HOST_USER,
                        [form.cleaned_data['email'],settings.EMAIL_HOST_USER],
                        fail_silently=False,
                        )
            cart.clear()
        return render(request, 'created.html',{'order':order})
    else:
        if request.user.is_authenticated:
            userProfile = UserProfile.objects.get(user=request.user)
            form = OrderCreateForm(initial={'address':userProfile.address,'phone':userProfile.phone})
        else:
            form = OrderCreateForm()
    return render(request, 'create.html', {'form': form,'cart':cart})

def create_paypal(request):
    cart = Cart(request)
    u = User.objects.get(id=1)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            else:
                order.user = u
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
                coupouns = Coupouns.objects.get(code=cart.coupon)
                coupouns.status = False
                coupouns.save()
            order.total = request.POST.get('total', False)
            order.save()
            for item in cart:
                try:
                    product = Product.objects.filter(id=item['product']['id'])
                except Product.DoesNotExist:
                    return None
                OrderItem.objects.create(
                    order=order,
                    product_id=item['product']['id'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            subject = "Thank you for your order"
            message = "Success to order"
            from_email = settings.EMAIL_HOST_USER
            to_email = list(form.cleaned_data['email'])
            send_mail(
                        subject,
                        message,
                        settings.EMAIL_HOST_USER,
                        [form.cleaned_data['email'],settings.EMAIL_HOST_USER],
                        fail_silently=False,
                        )
            cart.clear()
            # order_created.delay(order.id)
            request.session['order_id'] = order.id
            return redirect(reverse('payment:process'))
    else:
        if request.user.is_authenticated:
            try:
                userProfile = UserProfile.objects.get(user=request.user)
            except UserProfile.DoesNotExist:
                return None
            form = OrderCreateForm(initial={'address':userProfile.address,'phone':userProfile.phone})
        else:
            form = OrderCreateForm()
    return render(request, 'create_paypal.html', {'form': form,'cart':cart})
