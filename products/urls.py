from django.urls import path
from . import views
from .views import products

urlpatterns = [
    path('',views.products,name='products'),
    path('pr/<int:pr_id>', views.detail, name='detail'),
    path('cat/<int:pr_cat>', views.products_cat, name='products_cat'),
]
