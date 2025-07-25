from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model , authenticate, login, logout
from django.shortcuts import get_object_or_404
from .serializers import CustomUserSerializer
from rest_framework import status
from rest_framework.decorators import api_view


User  = get_user_model()
# Create your views here.
class CurrentUserView(APIView):
    
    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)

class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        role = data.get('role', 'student')  # Default to 'student'

        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return Response({'error': 'Missing required fields.'}, status=status.HTTP_400_BAD_REQUEST)

        if role not in ['student', 'teacher']:
            return Response({'error': 'Invalid role specified.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create user first
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # Set role flags if they exist on the model
        user.is_student = (role == 'student')
        user.is_teacher = (role == 'teacher')
        user.save()

        serializer = CustomUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutAPIView(APIView):
    permission_classes = [AllowAny] 
    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
    

@api_view(['GET'])
def check_login_status(request):
    if request.user.is_authenticated:
        return Response({'isAuthenticated': True, 'username': request.user.username})
    return Response({'isAuthenticated': False})