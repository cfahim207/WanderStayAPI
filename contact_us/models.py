from django.db import models

# Create your models here.
class Contact_Us(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    phone=models.IntegerField()
    message=models.TextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural ="Contact Us"