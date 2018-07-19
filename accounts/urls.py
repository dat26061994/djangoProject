from django.urls import path, include
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('userProfile', views.userProfile, name='userProfile'),
    path('userProfile/edit', views.editProfile, name='editProfile'),
]