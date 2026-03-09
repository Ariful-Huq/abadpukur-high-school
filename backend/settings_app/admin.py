from django.contrib import admin
from .models import SchoolClass, Subject

@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ("name", "section", "room_number")
    search_fields = ("name", "section")
    ordering = ("name",)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "assigned_teacher")
    search_fields = ("name", "code", "assigned_teacher__username")
    list_filter = ("assigned_teacher",)
    ordering = ("name",)