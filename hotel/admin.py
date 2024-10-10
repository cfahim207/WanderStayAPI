
from django.contrib import admin
from .import models
# Register your models here.
class HotelCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':
        ('name',),}
class HotelCountryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':
        ('name',),}
class HotelCityAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':
        ('name',),}
    
admin.site.register(models.HotelCategory,HotelCategoryAdmin)
admin.site.register(models.Country,HotelCountryAdmin)
admin.site.register(models.City,HotelCityAdmin)
admin.site.register(models.Hotel)

    
