from rest_framework import serializers
from .models import Contact_Us

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact_Us
        fields="__all__"