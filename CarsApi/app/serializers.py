from rest_framework import serializers
from .models import Car
from django.utils import timezone

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

    def validate_year(self, value):
        if value > timezone.now().year:
            raise serializers.ValidationError("Год выпуска не может быть больше текущего года.")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Цена должна быть положительным числом.")
        return value
    
    def validate_mileage(self, value):
        if value < 0:
            raise serializers.ValidationError("Пробег не может быть отрицательным числом.")
        return value


from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', '')
        )
        return user