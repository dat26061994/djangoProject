from django.contrib import admin
from .models import Slider,Category,Gallery

# Register your models here.
class postSlider(admin.ModelAdmin):
    list_display = ["name","title","image","Description","Status"]
    search_fields = ['name']

class postCategory(admin.ModelAdmin):
    list_display = ["name","title","image","status"]
    search_fields = ['name']
class postGallery(admin.ModelAdmin):
    list_display = ["image"]


admin.site.register(Slider,postSlider)
admin.site.register(Category,postCategory)
admin.site.register(Gallery,postGallery)
