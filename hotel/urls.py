from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HotelViewset,HotelCategoryViewset,CountryViewset,CityViewset,ReviewViewset

router = DefaultRouter()

router.register('list', HotelViewset,)
router.register('category', HotelCategoryViewset,)
router.register('country', CountryViewset,)
router.register('city', CityViewset,)
router.register('review', ReviewViewset,)

urlpatterns = [
    path('', include(router.urls)),
]