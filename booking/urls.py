from django.urls import path, include
from rest_framework.routers import DefaultRouter
from booking import views

router = DefaultRouter()

router.register('list', views.BookingViewset,)

urlpatterns = [
    path('', include(router.urls)),
]  