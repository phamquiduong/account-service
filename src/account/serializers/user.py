from rest_framework import serializers

from account.models import AuthUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        exclude = ("groups", "user_permissions")
        extra_kwargs = {
            # Password hash
            "password": {"write_only": True},
            # Verify data
            "phone_number_verified": {"read_only": True},
            "email_verified": {"read_only": True},
            # Permission
            "is_superuser": {"read_only": True},
            "is_staff": {"read_only": True},
            # State
            "is_active": {"read_only": True},
            # Tracking datetime
            "last_login": {"read_only": True},
            "date_joined": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }
