from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Student

# Register your models here.

class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'Student'

class CustomizedUserAdmin(UserAdmin): # Override inlines
    inlines = (StudentInline, )

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
