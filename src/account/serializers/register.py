from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework import serializers

from account.models import AuthUser


class RegisterSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    username = serializers.CharField(max_length=32, validators=[UnicodeUsernameValidator()])
    password = serializers.CharField(write_only=True, validators=[validate_password])

    def validate_username(self, username: str):
        if AuthUser.objects.filter(username=username).exists():
            raise serializers.ValidationError("username already exists", code="register.username.conflict")
        return username

    def create(self, validated_data: dict) -> AuthUser:
        return AuthUser.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
        )
