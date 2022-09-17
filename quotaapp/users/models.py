from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_user', null=True)
    std_id = models.CharField(max_length=10, verbose_name='Student ID', null=True)
    std_first = models.CharField(max_length=200, verbose_name='First Name', null=True)
    std_last = models.CharField(max_length=200, verbose_name='Last Name', null=True)
    b_date = models.DateField(verbose_name='Birth Date', blank=True, help_text='format: YYYY-MM-DD', null=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'),('Female', 'Female'),('Other', 'Other')], null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.std_id} {self.std_first} {self.std_last}'
        