from django.contrib import admin
from .models import TeacherProfile, Subject

@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ("teacher_id", "user", "designation")
    search_fields = ("teacher_id", "user__username", "user__first_name", "user__last_name")
    filter_horizontal = ("subjects",)
    ordering = ("teacher_id",)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "class_fk")
    search_fields = ("name",)
    list_filter = ("class_fk",)
    ordering = ("name",)