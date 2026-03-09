from django.db import models
from students.models import Student, Class, Section

class Attendance(models.Model):
    STATUS_CHOICES = [
        ("P", "Present"),
        ("A", "Absent"),
        ("L", "Late"),
        ("LV", "Leave"),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="attendances")
    class_fk = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="attendances")
    section_fk = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="attendances")
    date = models.DateField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("student", "date")
        ordering = ["-date", "class_fk", "section_fk"]

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"
