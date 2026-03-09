from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q
from .models import Period, ClassRoutine
from .serializers import PeriodSerializer, ClassRoutineSerializer

class PeriodViewSet(viewsets.ModelViewSet):
    queryset = Period.objects.all().order_by("start_time")
    serializer_class = PeriodSerializer

class ClassRoutineViewSet(viewsets.ModelViewSet):
    queryset = ClassRoutine.objects.all().order_by("day_of_week", "period")
    serializer_class = ClassRoutineSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        class_id = self.request.query_params.get("class")
        section_id = self.request.query_params.get("section")
        day = self.request.query_params.get("day")

        filters = Q()
        if class_id:
            filters &= Q(class_fk__id=class_id)
        if section_id:
            filters &= Q(section_fk__id=section_id)
        if day is not None:
            filters &= Q(day_of_week=day)
        return queryset.filter(filters).order_by("day_of_week", "period")

    @action(detail=False, methods=["post"])
    def bulk_create(self, request):
        routines = request.data.get("routines", [])
        serializer = ClassRoutineSerializer(data=routines, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
