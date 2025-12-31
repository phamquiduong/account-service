from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as AbstractUserManager
from django.db import models

from common.models import TimestampMixin, UUIDPrimaryMixin


class UserManager(AbstractUserManager):
    @classmethod
    def normalize_email(cls, email):
        if email is None:
            return None
        return super().normalize_email(email)


class AuthUser(AbstractUser, TimestampMixin, UUIDPrimaryMixin):
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    phone_number_verified = models.BooleanField(default=False)

    email = models.EmailField(unique=True, null=True, blank=True)
    email_verified = models.BooleanField(default=False)

    REQUIRED_FIELDS = []

    # Remove some fields
    first_name = None
    last_name = None

    objects = UserManager()

    def __str__(self) -> str:
        return f"<User: {self.id}>"

    class Meta:
        db_table = "auth_users"
