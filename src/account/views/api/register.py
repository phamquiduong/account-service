from drf_spectacular.utils import extend_schema
from rest_framework import generics

from account.serializers.register import RegisterSerializer


@extend_schema(tags=["Account"])
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
