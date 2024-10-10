from django.db import models
from customer.models import Customer
from hotel.models import Hotel
# Create your models here.

BOOKING_STATUS=[
    ('Complete','Complete'),
    ('Pending','Pending'),
]
class Booking(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    booking_status=models.CharField(choices=BOOKING_STATUS,max_length=10,default="Pending")
    stay_date=models.DateField(null=True)
    adults=models.IntegerField(null=True,blank=True)
    children=models.IntegerField(null=True,blank=True)
    cancel=models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.hotel.name
    