# backend/attendance/urls.py

from django.urls import path
from . import views
urlpatterns = [
    path('staff/',views.staff, name='staff'),
    path('store-student-data/',views.store_student_data,name='store_student_data')
]
