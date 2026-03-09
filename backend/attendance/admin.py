from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("student", "class_fk", "section_fk", "date", "status")
    list_filter = ("class_fk", "section_fk", "status", "date")
    search_fields = ("student__first_name", "student__last_name", "student__student_id")
    ordering = ("-date", "class_fk", "section_fk")