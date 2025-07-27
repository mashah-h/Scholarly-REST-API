from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny

from .serializers import CustomUserSerializer

User = get_user_model()

class CurrentUserView(APIView):
    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)

class RegisterUserView(APIView):
    http_method_names = ['post']
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already taken.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already registered.'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

@method_decorator(ensure_csrf_cookie, name='dispatch')
class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return Response({
                "message": "Login successful",
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "is_student": user.is_student,
                    "is_teacher": user.is_teacher
                }
            }, status=status.HTTP_200_OK)
        return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request):  # Optional: used to set the CSRF cookie
        return Response({'detail': 'CSRF cookie set'})

class LogoutAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_csrf_token(request):
    """
    View to get CSRF token for the current session.
    This is needed for CSRF protection in API requests.
    """
    return HttpResponse(status=204)

@api_view(['GET'])
def check_login_status(request):
    if request.user.is_authenticated:
        return Response({
            'isAuthenticated': True, 
            'user': {
                'id': request.user.id,
                'username': request.user.username,
                'email': request.user.email,
                'is_teacher': request.user.is_teacher,
                'is_student': request.user.is_student
            }
        })
    return Response({'isAuthenticated': False})
