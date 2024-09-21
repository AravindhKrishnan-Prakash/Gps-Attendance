from django.db import models

class StaffAttendance(models.Model):
    staff_name = models.CharField(max_length=100)
    batch = models.CharField(max_length=100)
    classroom = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    generated_code = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.staff_name} - {self.generated_code}"
class StudentAttendance(models.Model):
    student_name = models.CharField(max_length=255)
    roll_number = models.CharField(max_length=50)
    staff_name = models.CharField(max_length=255)
    subject_code = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    location = models.JSONField()
    code = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.subject_code} - {self.student_name}"