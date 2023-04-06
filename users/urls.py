from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import (EmailVerificationView, UserLoginView, UserProfile,
                    UserRegistrationView)

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile/<int:pk>/', UserProfile.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('verifi/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verification'),
]
