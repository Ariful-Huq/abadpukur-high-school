from django.contrib import admin
from .models import Fee

@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    list_display = ("student", "amount", "payment_method", "paid_by", "paid_at")
    list_filter = ("payment_method", "paid_at")
    search_fields = ("student__first_name", "student__last_name", "student__student_id", "paid_by__username")
    ordering = ("-paid_at",)