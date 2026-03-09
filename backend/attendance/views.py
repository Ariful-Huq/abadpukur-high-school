from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q
from datetime import date as today_date
from .models import Attendance
from .serializers import AttendanceSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all().order_by("-date", "class_fk", "section_fk")
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        class_id = self.request.query_params.get("class")
        section_id = self.request.query_params.get("section")
        date_param = self.request.query_params.get("date")

        filters = Q()
        if class_id:
            filters &= Q(class_fk__id=class_id)
        if section_id:
            filters &= Q(section_fk__id=section_id)
        if date_param:
            filters &= Q(date=date_param)
        else:
            filters &= Q(date=today_date())

        return queryset.filter(filters)

    @action(detail=False, methods=["post"])
    def bulk_create(self, request):
        """
        Accepts a list of attendance records to create or update.
        Expected format:
        {
            "attendances": [
                {
                    "student_id": 1,
                    "class_id": 2,
                    "section_id": 3,
                    "date": "2026-03-08",
                    "status": "P"
                },
                ...
            ]
        }
        """
        records = request.data.get("attendances", [])
        created_or_updated = []

        for rec in records:
            obj, created = Attendance.objects.update_or_create(
                student_id=rec["student_id"],
                date=rec["date"],
                defaults={
                    "class_fk_id": rec["class_id"],
                    "section_fk_id": rec["section_id"],
                    "status": rec["status"],
                },
            )
            created_or_updated.append(obj)

        serializer = AttendanceSerializer(created_or_updated, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
