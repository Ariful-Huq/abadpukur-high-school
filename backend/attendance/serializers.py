from rest_framework import serializers
from .models import Attendance
from students.serializers import StudentSerializer, ClassSerializer, SectionSerializer
from students.models import Student, Class, Section

class AttendanceSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), source="student", write_only=True
    )
    class_fk = ClassSerializer(read_only=True)
    class_id = serializers.PrimaryKeyRelatedField(
        queryset=Class.objects.all(), source="class_fk", write_only=True
    )
    section_fk = SectionSerializer(read_only=True)
    section_id = serializers.PrimaryKeyRelatedField(
        queryset=Section.objects.all(), source="section_fk", write_only=True
    )

    class Meta:
        model = Attendance
        fields = [
            "id",
            "student",
            "student_id",
            "class_fk",
            "class_id",
            "section_fk",
            "section_id",
            "date",
            "status",
            "created_at",
            "updated_at",
        ]
