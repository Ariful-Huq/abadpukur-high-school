from django.db import models
from users.models import User
from students.models import Class, Section

class Subject(models.Model):
    name = models.CharField(max_length=100)
    class_fk = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="subjects")

    def __str__(self):
        return f"{self.name} ({self.class_fk.name})"

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_id = models.CharField(max_length=20, unique=True, db_index=True)
    designation = models.CharField(max_length=100, blank=True)
    contact_number = models.CharField(max_length=20, blank=True)
    subjects = models.ManyToManyField(Subject, blank=True, related_name="teachers")

    def save(self, *args, **kwargs):
        if not self.teacher_id:
            self.teacher_id = self.generate_teacher_id()
        super().save(*args, **kwargs)

    def generate_teacher_id(self):
        school_code = "ABC"
        last_teacher = TeacherProfile.objects.order_by("-teacher_id").first()
        if last_teacher:
            number = int(last_teacher.teacher_id[-3:]) + 1
        else:
            number = 1
        return f"{school_code}T{number:03d}"

    def __str__(self):
        return f"{self.teacher_id} - {self.user.get_full_name()}"