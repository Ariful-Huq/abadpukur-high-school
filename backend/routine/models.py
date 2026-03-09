from django.db import models
from students.models import Class, Section
from teachers.models import TeacherProfile, Subject

class Period(models.Model):
    name = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.name} ({self.start_time} - {self.end_time})"

class ClassRoutine(models.Model):
    class_fk = models.ForeignKey(Class, on_delete=models.CASCADE)
    section_fk = models.ForeignKey(Section, on_delete=models.CASCADE)
    day_of_week = models.IntegerField(
        choices=[(0, "Sunday"), (1, "Monday"), (2, "Tuesday"), (3, "Wednesday"), (4, "Thursday")]
    )
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.SET_NULL, null=True)
    room_number = models.CharField(max_length=20, blank=True)

    class Meta:
        unique_together = ("class_fk", "section_fk", "day_of_week", "period")
        ordering = ("day_of_week", "period")

    def __str__(self):
        return f"{self.class_fk.name}-{self.section_fk.name} | {self.get_day_of_week_display()} | {self.period.name}"
    