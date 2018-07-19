from django.contrib import admin
from .models import Product,Product_Image,Product_Detail

# Register your models here.
class postProduct(admin.ModelAdmin):
    list_display = ["name","category","price","image","status"]
    search_fields = ['name']

class postProduct_Image(admin.ModelAdmin):
    list_display = ["image1","image2","image3"]

class postProduct_Detail(admin.ModelAdmin):
    list_display = ["weight","dimensions","materials","color","size"]

admin.site.register(Product,postProduct)
admin.site.register(Product_Image,postProduct_Image)
admin.site.register(Product_Detail,postProduct_Detail)
