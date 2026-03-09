from django.db import models
from datetime import datetime


class AcademicSession(models.Model):
    name = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=50)
    school_code = models.CharField(max_length=3, default="ABC")

    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=10)
    class_fk = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="sections")

    def __str__(self):
        return f"{self.class_fk.name}-{self.name}"

class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    student_id = models.CharField(max_length=20, unique=True, db_index=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[("M","Male"),("F","Female")])
    guardian_name = models.CharField(max_length=100, blank=True)
    guardian_contact = models.CharField(max_length=20, blank=True)
    class_fk = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, related_name="students")
    section_fk = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, blank=True, related_name="students")
    session = models.ForeignKey(AcademicSession, on_delete=models.SET_NULL, null=True, related_name="students")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.student_id:
            self.student_id = self.generate_student_id()
        super().save(*args, **kwargs)

    def generate_student_id(self):
        school_code = self.class_fk.school_code if self.class_fk else "ABC"
        year = self.session.start_date.strftime("%y") if self.session else datetime.now().strftime("%y")
        last_student = Student.objects.filter(student_id__startswith=f"{school_code}{year}").order_by("-student_id").first()
        if last_student:
            number = int(last_student.student_id[-3:]) + 1
        else:
            number = 1
        return f"{school_code}{year}{number:03d}"

    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"