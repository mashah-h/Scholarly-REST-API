from django.urls import path
from .views import CurrentUserView , RegisterUserView, LoginAPIView, LogoutAPIView , check_login_status
# from django.contrib.auth.views import LoginView, LogoutView
from .views import get_csrf_token


urlpatterns = [
    path('csrf/', get_csrf_token, name='csrf'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('user/', CurrentUserView.as_view(), name='current-user'),
    path('check-auth/', check_login_status, name='check-login-status'),
]

