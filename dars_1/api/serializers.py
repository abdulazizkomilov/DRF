from rest_framework import serializers
from products.models import Product, Category
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
from django.contrib.auth.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2',]

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': 'Password does not macht'})
        
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError(
                {'error': 'Email alrady exist'})
        
        account = User(
            email=self.validated_data['email'], 
            username=self.validated_data['username']
            )
        account.set_password(self.validated_data['password'])
        account.save()
        return account

def check_name(value):
    if len(value) <= 5:
        raise serializers.ValidationError("Name is too short")


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=150, validators=[
        UniqueValidator(queryset=Product.objects.all()), check_name
    ])
    avalible = serializers.IntegerField(
        required=True
    )

    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'price', 'description', 'image', 'avalible',]



class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=150)
    category = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
