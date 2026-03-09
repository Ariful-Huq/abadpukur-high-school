from rest_framework import serializers
from .models import TeacherProfile, Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"

class TeacherSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    subjects = SubjectSerializer(many=True, read_only=True)
    class Meta:
        model = TeacherProfile
        fields = "__all__"
