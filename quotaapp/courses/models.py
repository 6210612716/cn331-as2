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
        #  '[QUOTA: {self.quota}, STATUS: CLOSED]'
        if self.status == True:
            return f'{self.semester}/{self.year} {self.c_code} ({self.c_name})'
        else:
            return f'{self.semester}/{self.year} {self.c_code} ({self.c_name})'
