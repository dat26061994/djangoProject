from django.urls import path
from . import views

urlpatterns = [
    path('',views.contact,name='contact'),
    path('/send',views.send,name='send'),

]
