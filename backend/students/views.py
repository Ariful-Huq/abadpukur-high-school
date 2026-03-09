from rest_framework import viewsets
from .models import Student, Class, Section, AcademicSession
from .serializers import StudentSerializer, ClassSerializer, SectionSerializer, AcademicSessionSerializer



class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by("student_id")
    serializer_class = StudentSerializer


class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class AcademicSessionViewSet(viewsets.ModelViewSet):
    queryset = AcademicSession.objects.all()
    serializer_class = AcademicSessionSerializer
