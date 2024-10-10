from rest_framework import serializers
from .models import Customer,Deposite
from django.contrib.auth.models import User

class CustomerSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model= Customer
        fields='__all__'
        
class DepositSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(many=False, queryset=Customer.objects.all())  # For writing
    customer_display = serializers.StringRelatedField(many=False, source='customer', read_only=True)
    class Meta:
        model = Deposite
        fields = ['id','customer','customer_display', 'amount', 'timestamp']
    
    def create(self,validated_data):
        customer=validated_data["customer"]
        amount=validated_data["amount"]
        customer.balance+=amount
        customer.save()
    
        deposit=Deposite(**validated_data)
        deposit.save()
        return deposit
    
    
class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)
    image = serializers.CharField(max_length=350,default='',required=False)  # Image might be optional
    mobile = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'image', 'mobile']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        username = validated_data['username']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        password = validated_data['password']
        image = validated_data.get('image')
        mobile = validated_data['mobile']

        user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        user.set_password(password)
        user.is_active = False  # Assuming you want the user to be inactive initially
        user.save()

        # Create the related Customer object
        Customer.objects.create(
            user=user,
            image=image,
            mobile=mobile
        )

        return user
    
class UserLoginSerializer(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True)
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','first_name','last_name','email','is_superuser','date_joined']