from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from courses.models import Course
from .models import Student

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    else:
        all_students = Student.objects.all()
        if request.user.is_superuser:
            return render(request, 'users/index.html', {
                'all_students': all_students,
            })
        else:
            students = Student.objects.get(user=request.user)
            courses = Course.objects.filter(enrolled=students)
            return render(request, 'users/index.html', {
                'student_p': students,
                'courselist': courses,
        })

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('users:index'))
        else:
            return render(request, 'users/login.html', {'message': 'Invalid credentials.'})
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'users/login.html', {'message': 'You are logged out.'})
