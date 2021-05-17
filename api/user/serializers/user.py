from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login

from api.core.models.user import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def validate_berkeley_email(self, value):
        if not User.check_berkeley_email_valid(value):
            raise serializers.ValidationError("Berkeley email is invalid")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


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