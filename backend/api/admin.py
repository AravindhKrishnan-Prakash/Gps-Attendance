from django.contrib import admin
from .models import StaffAttendance
from . models import StudentAttendance
# Register the model with the admin site
admin.site.register(StaffAttendance)
admin.site.register(StudentAttendance)