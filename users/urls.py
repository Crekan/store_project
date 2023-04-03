from django.urls import path

from .views import UserLoginView, UserRegistrationView, UserProfile, logout

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile/<int:pk>/', UserProfile.as_view(), name='profile'),
    path('logout/', logout, name='logout'),
]
