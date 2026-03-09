from django.db import models
from users.models import User

class SchoolClass(models.Model):
    name = models.CharField(max_length=50)  # e.g., "Grade 6"
    section = models.CharField(max_length=5, blank=True)  # e.g., "A"
    room_number = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"{self.name} {self.section}".strip()

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    assigned_teacher = models.ForeignKey(
        User,
        limit_choices_to={'role__name': 'Teacher'},  # assuming Role model
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
