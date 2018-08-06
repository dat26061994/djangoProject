from django.contrib import admin
from .models import Product,Product_Image,Product_Detail,Review,Coupouns

# Register your models here.
class postProduct(admin.ModelAdmin):
    list_display = ["name","category","price","image","status"]
    search_fields = ['name']

class postProduct_Image(admin.ModelAdmin):
    list_display = ["image1","image2","image3"]

class postProduct_Detail(admin.ModelAdmin):
    list_display = ["weight","dimensions","materials","color","size"]

class postReview(admin.ModelAdmin):
    list_display = ["name","email","comments",'rating','created_at']

class postCoupouns(admin.ModelAdmin):
    list_display = ["code","discount","created_at",'status']

admin.site.register(Product,postProduct)
admin.site.register(Product_Image)
admin.site.register(Product_Detail)
admin.site.register(Review,postReview)
admin.site.register(Coupouns,postCoupouns)
