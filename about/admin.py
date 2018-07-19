from django.contrib import admin
from .models import About

# Register your models here.
class postAbout(admin.ModelAdmin):
    list_display = ["name","title","image","content","column"]
    search_fields = ['name']

admin.site.register(About,postAbout)
