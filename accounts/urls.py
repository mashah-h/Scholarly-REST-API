from django.urls import path
from .views import CurrentUserView , RegisterUserView, LoginAPIView, LogoutAPIView , check_login_status
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('me/', CurrentUserView.as_view(), name='current_user'),
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('login/', LoginAPIView.as_view(), name='login_user'),
    path('logout/', LogoutAPIView.as_view(), name='logout_user'), 
    path('check-auth/', check_login_status, name='check_login_status'), 
]

