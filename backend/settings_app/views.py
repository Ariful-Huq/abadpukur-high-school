from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import SchoolClass, Subject
from .serializers import SchoolClassSerializer, SubjectSerializer

class SchoolClassViewSet(viewsets.ModelViewSet):
    queryset = SchoolClass.objects.all()
    serializer_class = SchoolClassSerializer
    permission_classes = [IsAuthenticated]

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]
