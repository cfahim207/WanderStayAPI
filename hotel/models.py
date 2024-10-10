from django.db import models

# Create your models here.
class HotelCategory(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=70)
    
    def __str__(self):
        return self.name
    
class Country(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=70)
    
    def __str__(self):
        return self.name
    
class City(models.Model):
    country=models.ForeignKey(Country,on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=70)
    
    def __str__(self):
        return self.name
    
class Hotel(models.Model):
    name=models.CharField(max_length=200)
    descriptions=models.TextField()
    amount=models.IntegerField()
    image=models.CharField(max_length=350, default='')
    category=models.ManyToManyField(HotelCategory)
    country=models.ManyToManyField(Country)
    city=models.ManyToManyField(City)
    
    def __str__(self):
        return f'{self.name} - {self.amount} BDT'
    
    

    
STAR_CHOICE=[
    
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
]
    
class Review(models.Model):
    image=models.CharField(max_length=350,default="")
    name=models.CharField(max_length=20)
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    rating=models.CharField(choices=STAR_CHOICE, max_length=10)
    
    def __str__(self):
        return self.name  
    