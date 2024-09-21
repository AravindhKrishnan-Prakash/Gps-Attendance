from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import StaffAttendance
from .models import StudentAttendance
@api_view(['POST'])
def staff(request):
    if request.method == 'POST':
        staff_name = request.data.get('staff_name')
        batch = request.data.get('batch')
        classroom = request.data.get('classroom')
        subject = request.data.get('subject')
        generated_code = request.data.get('generated_code')

        # Create and save the attendance record
        attendance = StaffAttendance(
            staff_name=staff_name,
            batch=batch,
            classroom=classroom,
            subject=subject,
            generated_code=generated_code
        )
        attendance.save()

        return Response({"message": "Attendance data saved successfully"})
@api_view(['POST'])
def store_student_data(request):
    # Extract data from request
    if request.method == 'POST':
        student_name = request.data.get('studentName')
        roll_number = request.data.get('rollNumber')
        staff_name = request.data.get('staffName')
        subject_code = request.data.get('subjectCode')
        status = request.data.get('status')
        location = request.data.get('location')
        code = request.data.get('code')

        # Create a new StudentAttendance entry
        attendance = StudentAttendance(
            student_name=student_name,
            roll_number=roll_number,
            staff_name=staff_name,
            subject_code=subject_code,
            status=status,
            location=location,
            code=code
        )
        attendance.save()
        return Response({"message": "Attendance recorded successfully!"})
