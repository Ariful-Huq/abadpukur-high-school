from rest_framework import serializers
from .models import Fee

class FeeSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.first_name', read_only=True)
    paid_by_name = serializers.CharField(source='paid_by.username', read_only=True)

    class Meta:
        model = Fee
        fields = [
            "id",
            "student",
            "student_name",
            "amount",
            "payment_method",
            "paid_by",
            "paid_by_name",
            "paid_at",
            "description"
        ]
