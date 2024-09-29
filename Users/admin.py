from django.contrib import admin
from .models import StudentModel, Teachers, Group, Attendance, CoinTransaction

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'teacher', 'date', 'is_present')
    list_filter = ('date', 'is_present', 'teacher')
    search_fields = ('student__name', 'teacher__name')
    ordering = ('-date',)

class CoinTransactionAdmin(admin.ModelAdmin):
    list_display = ('student', 'teacher', 'date', 'coins')
    list_filter = ('date', 'coins', 'teacher')
    search_fields = ('student__name', 'teacher__name')
    ordering = ('-date',)

class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'coins', 'student_group']
    search_fields = ['name']
    ordering = ['name']

class TeachersAdmin(admin.ModelAdmin):
    list_display = ['name', 'lastname', 'phone', 'directory']
    search_fields = ['name', 'lastname', 'phone']
    ordering = ['lastname']

class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher']
    search_fields = ['name']
    ordering = ['name']

admin.site.register(StudentModel, StudentModelAdmin)
admin.site.register(Teachers, TeachersAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(CoinTransaction, CoinTransactionAdmin)
