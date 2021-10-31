from rest_framework import serializers
from django.contrib.auth import authenticate

from api.core.models import User
from api.major.serializers import MajorSerializer
from .userprofile import UserProfileSerializer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('berkeley_email', 'password')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def validate_berkeley_email(self, value):
        if not User.check_berkeley_email_valid(value):
            raise serializers.ValidationError("Berkeley email is invalid")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserDetailSerializer(serializers.ModelSerializer):

    user_profile = UserProfileSerializer(source='current_profile')
    majors = MajorSerializer(many=True)
    minors = MajorSerializer(many=True)

    class Meta:
        model = User
        exclude = ('password',)
        read_only_fields = ('id',)


class UserLoginSerializer(serializers.Serializer):
    """Serializer used for login"""
    berkeley_email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        berkeley_email = data.get("berkeley_email", None)
        password = data.get("password", None)
        user = authenticate(berkeley_email=berkeley_email, password=password)
        if not user:
            raise serializers.ValidationError("Invalid auth credentials")
        data['user'] = user
        return user


class UserSignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('berkeley_email', 'password', 'first_name', 'last_name', 'full_name', 'country', 'gender', 'birth', 'majors', 'minors')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def validate_berkeley_email(self, value):
        if not User.check_berkeley_email_valid(value):
            raise serializers.ValidationError("Berkeley email is invalid")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user