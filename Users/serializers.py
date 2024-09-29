from rest_framework import serializers
from .models import *


# class SutendtLoginSRL(serializers.ModelSerializer):
#     class Meta:
#         model = StudentModel
#         fields = ['modme_id', 'password']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ['name', 'lastname', 'phone', 'directory', 'password']


class HammaStudentlarSerializeri(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = "__all__"


class OquvchiIsmi(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = ('name',)
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"


class CoinTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinTransaction
        fields = "__all__"
