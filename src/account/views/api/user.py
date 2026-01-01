from rest_framework import generics

from account.models import AuthUser
from account.serializers.user import UserSerializer


class UserListView(generics.ListAPIView):
    queryset = AuthUser.objects.all()
    serializer_class = UserSerializer
