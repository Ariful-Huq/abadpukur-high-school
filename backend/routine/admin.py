from django.contrib import admin
from .models import Period, ClassRoutine

@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ("name", "start_time", "end_time")
    ordering = ("start_time",)

@admin.register(ClassRoutine)
class ClassRoutineAdmin(admin.ModelAdmin):
    list_display = ("class_fk", "section_fk", "day_of_week", "period", "subject", "teacher", "room_number")
    list_filter = ("class_fk", "section_fk", "day_of_week", "period")
    search_fields = ("class_fk__name", "section_fk__name", "subject__name", "teacher__teacher_id")
    ordering = ("day_of_week", "period")