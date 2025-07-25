from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentProfileViewSet,SubjectViewSet, MarksViewSet


router = DefaultRouter()
router.register(r'students', StudentProfileViewSet, basename='student-profile')
router.register(r'subjects', SubjectViewSet, basename='subject')
router.register(r'marks', MarksViewSet, basename='marks')   

urlpatterns = [
    path('', include(router.urls)),

]
