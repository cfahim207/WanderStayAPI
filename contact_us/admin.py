from django.contrib import admin
from .models import Contact_Us
# Register your models here.

class ContactUsmodelAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','message']
    
    
admin.site.register(Contact_Us,ContactUsmodelAdmin)