from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer,Deposite
from .serializer import CustomerSerializer,RegistrationSerializer,UserLoginSerializer,DepositSerializer,UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
from rest_framework import generics
from contact_us.models import Contact_Us
from contact_us.serializer import ContactUsSerializer
from booking.models import Booking
from booking.serializer import BookingSerializer
from hotel.models import Hotel,Country,City,Review,HotelCategory
from hotel.serializer import HotelSerializer,HotelCategorySerializer,CountrySerializer,CitySerializer,ReviewSerializer
from rest_framework.permissions import AllowAny
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class CustomerViewset(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
    
    def get_queryset(self):
        queryset=super().get_queryset()
        id=self.request.query_params.get("id")
        if id:
            queryset=queryset.filter(id=id)
        return queryset
    
class DepositeViewset(viewsets.ModelViewSet):
    queryset=Deposite.objects.all()
    serializer_class=DepositSerializer
    
    
class UserRegistrationView(APIView):
    serializer_class = RegistrationSerializer
    
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user=serializer.save()
            token=default_token_generator.make_token(user)
            uid=urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link=f'https://wander-stay-api.vercel.app/customer/active/{uid}/{token}'
            email_subject="Confirm Your Email"
            email_body=render_to_string("confirm_email.html",{'confirm_link': confirm_link})
            email=EmailMultiAlternatives(email_subject,'',to=[user.email])
            email.attach_alternative(email_body,'text/html')
            email.send()
            return Response('Check your mail for confirmation')
        return Response(serializer.errors)


def activate(request,uid64,token):
    try:
        uid=urlsafe_base64_decode(uid64).decode()
        user=User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user=None
        
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        return redirect("https://cfahim207.github.io/WanderStay-Frontend/login.html")
    else:
        return redirect('register')
    
    
class UserLoginApiView(APIView):
    def post(self,request):
        serializer=UserLoginSerializer(data=self.request.data)
        if serializer.is_valid():
            username=serializer.validated_data['username']
            password=serializer.validated_data['password']
            print(username,password)
            
            user=authenticate(username=username,password=password)
            
            
            if user:
                token,_=Token.objects.get_or_create(user=user)
                customer,_=Customer.objects.get_or_create(user=user)
                login(request,user)
                return Response({'token': token.key,'user_id': user.id,'customer_id':customer.id})

            else:
                return Response({'error':'Invalid Credential'})
        
        return Response(serializer.errors)
    

# class UserlogoutView(APIView):
#     def get(self,request):
#         request.user.auth_token.delete()
#         logout(request)
#         return redirect("login")

@method_decorator(csrf_exempt, name='dispatch')
class UserlogoutapiView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response({"message":"logout Successfully"})
    
    
class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user
    
class DashboardView(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            # Admin Dashboard
            customer = Customer.objects.all()
            deposite = Deposite.objects.all()
            booking = Booking.objects.all()
            hotel=Hotel.objects.all()
            country=Country.objects.all()
            category=HotelCategory.objects.all()
            city=City.objects.all()
            review=Review.objects.all()
            contactus=Contact_Us.objects.all()
            

            return Response({
                "customer": CustomerSerializer(customer, many=True).data,
                "user": UserSerializer(request.user).data,
                "deposite": DepositSerializer(deposite, many=True).data,
                "booking": BookingSerializer(booking, many=True).data,
                "hotel": HotelSerializer(hotel, many=True).data,
                "country": CountrySerializer(country, many=True).data,
                "category": HotelCategorySerializer(category, many=True).data,
                "city": CitySerializer(city, many=True).data,
                "review": ReviewSerializer(review, many=True).data,
                "contact_us": ContactUsSerializer(contactus, many=True).data
            })
        else:
            # Regular User Dashboard
            customer = request.user.customer
            deposite = Deposite.objects.filter(customer=customer)
            booking = Booking.objects.filter(customer=customer)
            

            return Response({
                "profile": CustomerSerializer(customer).data,
                "user": UserSerializer(request.user).data,
                "deposite": DepositSerializer(deposite, many=True).data,
                "booking": BookingSerializer(booking, many=True).data
            })
            