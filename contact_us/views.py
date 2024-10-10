from django.shortcuts import render
from rest_framework import viewsets
from .models import Contact_Us
from .serializer import ContactUsSerializer
# Create your views here.

class ContactUsViewset(viewsets.ModelViewSet):
    queryset=Contact_Us.objects.all()
    serializer_class=ContactUsSerializer