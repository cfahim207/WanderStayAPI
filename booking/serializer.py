from rest_framework import serializers
from .models import Booking
from hotel.models import Hotel
from customer.models import Customer

class BookingSerializer(serializers.ModelSerializer):
    hotel = serializers.PrimaryKeyRelatedField(many=False,queryset=Hotel.objects.all())  # For writing
    hotel_display = serializers.StringRelatedField(many=False, source='hotel', read_only=True)  # For reading
    customer = serializers.PrimaryKeyRelatedField(many=False,queryset=Customer.objects.all())  # For writing
    customer_display = serializers.StringRelatedField(many=False, source='customer', read_only=True)  # For reading
    
    class Meta:
        model= Booking
        fields=['id','hotel','hotel_display','customer','customer_display','stay_date','adults','children','cancel','booking_status']
        
    def create(self,validated_data):
        hotel=self.validated_data["hotel"]
        booker=self.validated_data["customer"]
        if booker.balance<hotel.amount:
            raise serializers.ValidationError({'error': "Insufficient balance"})
        else:
            booker.balance-=hotel.amount
            booker.save()
        validated_data['booking_status'] = "Complete"
        booking=Booking(**validated_data)
        booking.save()
        return booking
    
        