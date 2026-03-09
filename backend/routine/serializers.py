from rest_framework import serializers
from students.models import Class, Section
from teachers.models import TeacherProfile, Subject
from .models import Period, ClassRoutine

class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = "__all__"

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ["id", "name"]

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ["id", "name", "class_fk"]

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["id", "name"]

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = ["id", "teacher_id", "user"]

class ClassRoutineSerializer(serializers.ModelSerializer):
    class_fk = ClassSerializer(read_only=True)
    class_id = serializers.PrimaryKeyRelatedField(
        queryset=Class.objects.all(), source="class_fk", write_only=True
    )
    section_fk = SectionSerializer(read_only=True)
    section_id = serializers.PrimaryKeyRelatedField(
        queryset=Section.objects.all(), source="section_fk", write_only=True
    )
    subject = SubjectSerializer(read_only=True)
    subject_id = serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all(), source="subject", write_only=True
    )
    teacher = TeacherSerializer(read_only=True)
    teacher_id = serializers.PrimaryKeyRelatedField(
        queryset=TeacherProfile.objects.all(), source="teacher", write_only=True
    )

    class Meta:
        model = ClassRoutine
        fields = [
            "id",
            "class_fk",
            "class_id",
            "section_fk",
            "section_id",
            "period",
            "subject",
            "subject_id",
            "teacher",
            "teacher_id",
            "day_of_week",
            "room_number",
        ]
