from django.db import models
from students.models import Student
from users.models import User

PAYMENT_METHOD_CHOICES = (
    ('cash', 'Cash'),
    ('mfs', 'Mobile Financial Service'),
    # 'bank_transfer' can be added later
)

class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='fees')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    paid_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    paid_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.amount} via {self.payment_method}"
    