from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('userProfile', views.userProfile, name='userProfile'),
    path('userProfile/edit', views.editProfile, name='editProfile'),
    path('userProfile/editAvatar', views.editAvatar, name='editAvatar'),
    path('userProfile/changePassword', views.changePassword, name='changePassword'),
    path('userProfile/ordersInfor', views.ordersInfor, name='ordersInfor'),
    path('userProfile/ordersInfor/<int:order_id>', views.orderDetail, name='orderDetail'),
    path('userProfile/wishlist', views.wishlist, name='wishlist'),
    path('userProfile/addWishlist', views.addWishlist, name='addWishlist'),
    path('userProfile/delwishlist/<int:id>', views.delwishlist, name='delwishlist'),
    path(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    path(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    path(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]
