from rest_framework import viewsets, permissions
from .models import (StudentProfile,Subject,Marks)
from .serializers import (StudentProfileSerializer, SubjectSerializer, MarksSerializer)
# Create your views here.

class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticated]  


class MarksViewSet(viewsets.ModelViewSet):
    queryset = Marks.objects.all()
    serializer_class = MarksSerializer
    permission_classes = [permissions.IsAuthenticated]