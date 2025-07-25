from django.db import models
from django.conf import settings

# Create your models here.
class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    admission_number = models.CharField(max_length=20 , unique= True)

    def __str__(self):
        return self.user.username
    

class Subject(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name
    

class Marks(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.FloatField(max_length=10)
    term = models.CharField(max_length=10)


    def __str__(self):
        return f"{self.student} - {self.subject}  -{self.term}"