from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    url(r'^$', views.cart_detail, name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^update/(?P<product_id>\d+)/$', views.cart_update, name='cart_update'),
    url(r'^coupon_apply/$',views.coupon_apply,name='coupon_apply'),
    url(r'^addajax/(?P<product_id>\d+)/$', views.cart_addajax, name='cart_addajax'),
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
]
