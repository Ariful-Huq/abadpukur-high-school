from rest_framework import serializers
from .models import SchoolClass, Subject

class SchoolClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolClass
        fields = ['id', 'name', 'section', 'room_number']

class SubjectSerializer(serializers.ModelSerializer):
    assigned_teacher_name = serializers.CharField(source='assigned_teacher.username', read_only=True)

    class Meta:
        model = Subject
        fields = ['id', 'name', 'code', 'assigned_teacher', 'assigned_teacher_name']
