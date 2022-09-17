from django.db import models
from users.models import Student

# Create your models here.

SEMESTER = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
)

class Course(models.Model):
    c_code = models.CharField(max_length=5, verbose_name='Course Code', null=True) 
    c_name = models.CharField(max_length=200, verbose_name='Course Name', null=True)
    semester = models.PositiveIntegerField(null=True, choices=SEMESTER)
    year = models.CharField(max_length=4, null=True)
    quota = models.PositiveIntegerField(null=True)
    # status = models.CharField(max_length=50, choices=STATUS, null=True)
    status = models.BooleanField(verbose_name='Course Status', default=True, help_text='Check = Open, Uncheck = Close')
    enrolled = models.ManyToManyField(Student, blank=True, related_name='enrolled')

    def __str__(self):
        if self.status == True:
            return f'{self.semester}/{self.year} {self.c_code} ({self.c_name}) [QUOTA: {self.quota}, STATUS: OPENED]'
        else:
            return f'{self.semester}/{self.year} {self.c_code} ({self.c_name}) [QUOTA: {self.quota}, STATUS: CLOSED]'

class Quota(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='courses', null=True)
    student = models.ForeignKey('users.Student', on_delete=models.CASCADE, related_name='students', null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        # return f'{self.course} [Enrolled Date {self.date_created} by: {self.student}]'
        return f'{self.course.semester}/{self.course.year} {self.course.c_code} ({self.course.c_name}) on {self.date_created}'
