from django.urls import path
from .views import AllStudents, BittaOquvchi, UpdateCoins, TeacherRegister, TeacherLogin,MarkAttendance


urlpatterns = [
    path('hammaoquvchi/', AllStudents.as_view()),
    path('bitta/', BittaOquvchi.as_view()),
    path('mark-attendance/', MarkAttendance.as_view()),
    path('update-coins/', UpdateCoins.as_view()),
    path('register/', TeacherRegister.as_view()),  # Add this line
    path('login/', TeacherLogin.as_view()),
]
