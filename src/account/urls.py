from django.urls import include, path

from account.views.api.register import RegisterView

api_router = [
    path("register", RegisterView.as_view(), name="account_register"),
]

urlpatterns = [
    path("api/", include(api_router)),
]
