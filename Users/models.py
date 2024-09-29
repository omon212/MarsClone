from  django.db import models
from django.contrib.auth.hashers import make_password, check_password

class StudentModel(models.Model):
    modme_id = models.BigIntegerField(unique=True)
    password = models.BigIntegerField(default=4321)
    name = models.CharField(max_length=32)
    coins = models.IntegerField()
    student_group = models.IntegerField(null=True)

    def str(self):
        return self.name



class Teachers(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)
    direc = (
        ("Fronted", 'Fronted'),
        ("Backend", 'Backend'),
        ("Design", 'Design'),
        ("Starter", 'Starter')
    )
    directory = models.CharField(max_length=200, choices=direc)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=20)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    students = models.ManyToManyField( StudentModel )
    coins = models.IntegerField()

    def str(self):
        return self.name

class Attendance(models.Model):
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.name} - {self.date} - {'Present' if self.is_present else 'Absent'}"


class CoinTransaction(models.Model):
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    coins = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.coins} coins"
