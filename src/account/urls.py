from django.urls import include, path

from account.views.api.register import RegisterView
from account.views.api.user import UserListView

api_router = [
    path("register", RegisterView.as_view(), name="account_register"),
    path("users", UserListView.as_view(), name="account_user_list"),
]

urlpatterns = [
    path("api/", include(api_router)),
]
