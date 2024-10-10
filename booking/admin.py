from django.contrib import admin
from .models import Booking
# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display=['hotel_name','customer_name','booking_status','stay_date']
    
    def hotel_name(self,obj):
        return obj.hotel.name
    def customer_name(self,obj):
        return obj.customer.user.first_name
    
admin.site.register(Booking,BookingAdmin)