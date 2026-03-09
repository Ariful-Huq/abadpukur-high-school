from django.contrib import admin
from .models import Student, Class, Section, AcademicSession

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "first_name", "last_name", "class_fk", "section_fk", "session")
    search_fields = ("student_id", "first_name", "last_name")
    list_filter = ("class_fk", "section_fk", "session")
    ordering = ("student_id",)

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ("name", "school_code")
    ordering = ("name",)

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("name", "class_fk")
    ordering = ("class_fk", "name")

@admin.register(AcademicSession)
class AcademicSessionAdmin(admin.ModelAdmin):
    list_display = ("name", "start_date", "end_date")
    ordering = ("start_date",)