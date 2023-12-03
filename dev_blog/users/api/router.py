from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.api.views import RegisterView, UserView, UserChangePasswordView

urlpatterns = [
  path('auth/register/', RegisterView.as_view(), name='register'),
  path('auth/me/', UserView.as_view(), name='me'),
  path('auth/update-password/', UserChangePasswordView.as_view(), name='update-password'),
  path('auth/login/', TokenObtainPairView.as_view(), name='login'),
  path('auth/refresh/', TokenRefreshView.as_view(), name='refresh'),
]