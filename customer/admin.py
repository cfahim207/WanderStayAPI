from django.contrib import admin
from .models import Customer,Deposite
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','mobile']
    
    def first_name(self,obj):
        return obj.user.first_name
    def last_name(self,obj):
        return obj.user.last_name
    
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Deposite)