from django.contrib import admin
from .models import StudentProfile, Subject , Marks

# Register your models here.
admin.site.register(StudentProfile)
admin.site.register(Subject)
admin.site.register(Marks)