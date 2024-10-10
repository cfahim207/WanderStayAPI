from django.shortcuts import render
from .models import Hotel,HotelCategory,Country,City,Review
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status 
from .serializer import HotelSerializer,HotelCategorySerializer,CountrySerializer,CitySerializer,ReviewSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, pagination
# Create your views here.

class HotelViewset(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category','country','city']
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        hotel = self.get_object()
        serializer = self.get_serializer(hotel, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    
    def get_queryset(self):
        queryset=super().get_queryset()
        id=self.request.query_params.get("id")
        if id:
            queryset=queryset.filter(id=id)
        return queryset
    
class HotelCategoryViewset(viewsets.ModelViewSet):
    queryset = HotelCategory.objects.all()
    serializer_class = HotelCategorySerializer
    
class CountryViewset(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    
class CityViewset(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    
class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer