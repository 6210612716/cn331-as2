from django.test import TestCase, Client
from .models import Course
from users.models import Student
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.

class CourseViewsTestCase(TestCase):
    def setUp(self):

        # create user
        self.client = Client()
        self.user = User.objects.create_user(username='6210612716', password='lio12345', )
        self.client.login(username='6210612716', password='lio12345')

        # create student
        student = Student.objects.create(user=User.objects.first())

        # create course
        course1 = Course.objects.create(
            c_code='CN111', c_name='Course 1', semester=1, year='2022', 
            quota=2, status=True, )
        course2 = Course.objects.create(
            c_code='CN222', c_name='Course 2', semester=2, year='2022', 
            quota=0, status=False, )
        
        course1.enrolled.add(student)
        course2.enrolled.add(student)

    def test_course_view_views_status_code(self):
        """ course_view view's status is ok """

        c = Client()
        c.login(username='6210612716', password='lio12345')
        response = c.get(reverse('courses:course_view'))
        self.assertEqual(response.status_code, 200)

    def test_search_views_status_code(self):
        """ search view's status is ok """

        c = Client()
        response = c.get(reverse('courses:search'))
        self.assertEqual(response.status_code, 200)

    def test_course_view_user_is_not_authenticated(self):
        """ user is not authenticated """
        
        self.client = Client()
        response = self.client.get(reverse('courses:course_view'))
        self.assertEqual(response.status_code, 302)

    def test_enroll(self):
        """ user can enroll course """

        student = Student.objects.first()
        course = Course.objects.first()
        self.client = Client()
        self.client.post(reverse('courses:enroll'), {'user': student.user, 'enroll': course.id})
        self.assertEqual(Course.objects.get(c_code=course.c_code).quota, 1)

    def test_cancel_enroll(self):
        """ user can cancel enroll """

        student = Student.objects.first()
        course = Course.objects.first()
        self.client = Client()
        self.client.post(reverse('courses:cancel'), {'user': student.user, 'cancel': course.id})
        self.assertEqual(Course.objects.get(c_code=course.c_code).quota, 3)
    