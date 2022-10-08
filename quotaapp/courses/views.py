from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Course
from users.models import Student

# Create your views here.

def course_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    else:
        all_courses = Course.objects.all().order_by('c_name')
        student = Student.objects.get(user=request.user)
        en_courses = Course.objects.filter(enrolled=student)
        students = Student.objects.get(user=request.user.id)
        return render(request, 'users/enroll.html', {
            'courselist': all_courses,
            'course_enrolled': en_courses,
            'std': students,
        })

def enroll(request):
    if request.method == 'POST':
        course = Course.objects.get(pk=request.POST['enroll'])
        student = Student.objects.get(user__username=request.POST['user'])
        Course.objects.filter(pk=request.POST['enroll']).update(quota=(course.quota-1))
        course.enrolled.add(student)
        return HttpResponseRedirect(reverse('courses:course_view'))
    
def cancel(request):
    if request.method == 'POST':
        course = Course.objects.get(pk=request.POST['cancel'])
        student = Student.objects.get(user__username=request.POST['user'])
        Course.objects.filter(pk=request.POST['cancel']).update(quota=(course.quota+1))
        course.enrolled.remove(student)
        return HttpResponseRedirect(reverse('courses:course_view'))

def search(request):
    return HttpResponse('Please go back.')
