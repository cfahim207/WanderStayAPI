from django.shortcuts import render
from rest_framework import viewsets
from .models import Booking
from .serializer import BookingSerializer
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class BookingViewset(viewsets.ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer
    
    def perform_create(self, serializer):
        # Save the order instance
        booking = serializer.save()

        # Send an email to the customer
        email_subject="Congratulation for successfully Booking.."
        email_body=render_to_string("confirm_booking.html",{'user':booking.customer.user, 'hotel':booking.hotel})
        email=EmailMultiAlternatives(email_subject,'',to=[booking.customer.user.email])
        email.attach_alternative(email_body,'text/html')
        email.send()
        
        
    def get_queryset(self):
        queryset=super().get_queryset()
        customer_id=self.request.query_params.get("customer_id")
        if customer_id:
            queryset=queryset.filter(customer_id=customer_id)
        return queryset
 