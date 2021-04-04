from django.urls import path
from .views import (RegisterationView, VerifyEmail,
ResetPassword, LogOut, HandleResetPassword)
from rest_framework_simplejwt.views import(TokenObtainPairView,
TokenRefreshView)

app_name = "Users"

urlpatterns = [
    path('register/', RegisterationView.as_view(),
    name="registeration"),

    path('token/', TokenObtainPairView.as_view(),
    name="get-token"),

    path('token/refresh/', TokenRefreshView.as_view(),
    name="refresh-token"),

    path('verify-email/', VerifyEmail.as_view(),
    name="verify"),

    path('resetpassword/', ResetPassword.as_view(),
    name="restpass"),

    path('changepassword/', HandleResetPassword.as_view(),
    name="changepass"),

    path('logout/', LogOut.as_view(),
    name="logout")
]