from rest_framework import viewsets
from .models import TeacherProfile, Subject
from .serializers import TeacherSerializer, SubjectSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = TeacherProfile.objects.all().order_by("teacher_id")
    serializer_class = TeacherSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all().order_by("name")
    serializer_class = SubjectSerializer
