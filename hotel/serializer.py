from rest_framework import serializers
from .models import Hotel,HotelCategory,Country,City,Review

class HotelSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(many=True, queryset=HotelCategory.objects.all())  # For writing
    category_display = serializers.StringRelatedField(many=True, source='category', read_only=True)  # For reading
    country = serializers.PrimaryKeyRelatedField(many=True, queryset=Country.objects.all())  # For writing
    country_display = serializers.StringRelatedField(many=True, source='country', read_only=True)  # For reading
    city = serializers.PrimaryKeyRelatedField(many=True, queryset=City.objects.all())  # For writing
    city_display = serializers.StringRelatedField(many=True, source='city', read_only=True)  # For reading

    class Meta:
        model = Hotel
        fields = ['id','category', 'category_display', 'country', 'country_display','city','city_display','image', 'name', 'amount','descriptions',]


        
class HotelCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=HotelCategory
        fields="__all__"
        
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields="__all__"
class CitySerializer(serializers.ModelSerializer):
    country = serializers.PrimaryKeyRelatedField(many=False, queryset=Country.objects.all())  # For writing
    country_display = serializers.StringRelatedField(many=False, source='country', read_only=True)  # For 
    class Meta:
        model=City
        fields=['id','country','country_display','name','slug']
        
class ReviewSerializer(serializers.ModelSerializer):
    hotel = serializers.PrimaryKeyRelatedField(many=False, queryset=Hotel.objects.all())  # For writing
    hotel_display = serializers.StringRelatedField(many=False, source='hotel', read_only=True)  # For reading
    
    class Meta:
        model=Review
        fields=['id','hotel','hotel_display','image','name','body','created','rating']
        