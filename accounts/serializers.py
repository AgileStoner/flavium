from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'phone_number', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True},
                              'id': {'read_only': True}}
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'phone_number', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True},
                              'id': {'read_only': True}}

    def validate(self, data):
        phone_number = data.get("phone_number", None)
        username = data.get("username", None)
        password = data.get("password", None)
        if not phone_number:
            raise serializers.ValidationError(
                'A phone number is required to register.'
            )
        if not username:
            raise serializers.ValidationError(
                'A username is required to register.'
            )
        if not password:
            raise serializers.ValidationError(
                'A password is required to register.'
            )
        if User.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError(
                'A user with this phone number already exists.'
            )
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                'A user with this username already exists.'
            )
        return data
    
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            phone_number=validated_data['phone_number'],
            password=validated_data['password'],
        )
        return user



class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        phone_number = data.get("phone_number", None)
        password = data.get("password", None)
        if not phone_number:
            raise serializers.ValidationError(
                'A phone number is required to login.'
            )
        if not password:
            raise serializers.ValidationError(
                'A password is required to login.'
            )
        if not User.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError(
                'A user with this phone number does not exist.'
            )
        user = authenticate(phone_number=phone_number, password=password)
        if not user:
            raise serializers.ValidationError(
                'A user with this phone number and password was not found.'
            )
        data['user'] = user
        return data