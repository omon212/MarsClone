from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import HammaStudentlarSerializeri,OquvchiIsmi
from rest_framework.response import Response
from .models import StudentModel
from rest_framework import status
from django.contrib.auth.hashers import check_password
from .serializers import TeacherSerializer
class TeacherRegister(APIView):
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Teacher registered successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherLogin(APIView):
    def post(self, request):
        phone = request.data.get('phone')
        password = request.data.get('password')

        try:
            teacher = Teachers.objects.get(phone=phone)
            if check_password(password, teacher.password):
                return Response({'message': 'Login successful!'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid password!'}, status=status.HTTP_401_UNAUTHORIZED)
        except Teachers.DoesNotExist:
            return Response({'message': 'Teacher not found!'}, status=status.HTTP_404_NOT_FOUND)

class AllStudents(APIView):
    def get(self,request):
        oquvchilar = StudentModel.objects.all()
        serializer = HammaStudentlarSerializeri(oquvchilar,many=True)
        return Response(serializer.data)


class BittaOquvchi(APIView):
    serializer_class = OquvchiIsmi

    def post(self,request):
        ismi = request.data.get('name')
        oquvchi = StudentModel.objects.all().filter(name = ismi)

        if oquvchi:
            serializer = HammaStudentlarSerializeri(oquvchi, many=True)
            return Response(serializer.data)
        else:
            return Response({'Message': "User Not Found"})



class MarkAttendance(APIView):
    def post(self, request):
        student_id = request.data.get('student_id')
        teacher_id = request.data.get('teacher_id')
        is_present = request.data.get('is_present')

        try:
            student = StudentModel.objects.get(id=student_id)
            teacher = Teachers.objects.get(id=teacher_id)
        except (StudentModel.DoesNotExist, Teachers.DoesNotExist):
            return Response({'message': 'Student or Teacher not found'}, status=404)

        # Mark attendance
        attendance = Attendance(student=student, teacher=teacher, is_present=is_present)
        attendance.save()
        return Response({'message': f"Attendance marked as {'Present' if is_present else 'Absent'} for {student.name}"})


class UpdateCoins(APIView):
    def post(self, request):
        student_id = request.data.get('student_id')
        coins_to_update = request.data.get('coins')

        try:
            student = StudentModel.objects.get(modme_id=student_id)
            student.coins += coins_to_update
            student.save()

            return Response(
                {
                    'message': f"Coins updated successfully. New balance: {student.coins}"
                },
                status=status.HTTP_200_OK
            )
        except StudentModel.DoesNotExist:
            return Response(
                {'message': "Student not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {'message': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )