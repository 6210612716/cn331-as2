from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Course, Quota
from users.models import Student

# Create your views here.

def course_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    else:
        if request.user.is_superuser:
            pass
        courses = Course.objects.all().order_by('c_name')
        student = Student.objects.get(user=request.user.id)
        enrolled = Student.objects.get(user=request.user)
        enrolled = Quota.objects.filter(student=enrolled)
        return render(request, 'users/enroll.html', {
            'courselist': courses,
            'std': student,
            'enrolled': enrolled,
        })

def enroll(request):
    course = Course.objects.get(pk=request.POST['enroll'])
    student = Student.objects.get(user=request.user.id)
    course.enrolled.add(student)
    Quota.objects.create(course=course, student=student)
    course.quota -= 1
    course.save()
    return HttpResponseRedirect(reverse('courses:course_view'))
    
def cancel(request):
    course = Course.objects.get(pk=request.POST['cancel'])
    student = Student.objects.get(user=request.user.id)
    enroll = Quota.objects.get(course=course, student=student)
    enroll.delete()
    course.quota += 1
    course.enrolled.remove(student)
    course.save()
    return HttpResponseRedirect(reverse('courses:course_view'))

def search(request):
    return HttpResponse('Please go back.')
