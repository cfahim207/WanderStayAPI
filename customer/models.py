from django.db import models
from django.contrib.auth.models import User
# Create your models here.
    
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.CharField(max_length=350,default="")
    mobile=models.CharField(max_length=12)
    balance=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f"{self.user.first_name}{self.user.last_name}"
    
class Deposite(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.customer.user.username} - {self.amount} on {self.timestamp}"