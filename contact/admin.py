from django.contrib import admin
from .models import Contact

# Register your models here.
class postContact(admin.ModelAdmin):
    list_display = ["address","phone","email"]

admin.site.register(Contact,postContact)
