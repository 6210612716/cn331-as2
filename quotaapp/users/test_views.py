from django.test import TestCase, Client
from courses.models import Course
from .models import Student
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.

class StudentViewsTestCase(TestCase):
    def setUp(self):
        User.objects.create_superuser(username='6210612716', password='lio12345')
        User.objects.create_user(username='6210612717', password='lio12345')

        Student.objects.create(
            user=User.objects.first(), std_id='6210612716', std_first='Puchit', 
            std_last='Kleebmalai', b_date='2000-05-22', gender='Male', email='pu@ex.com',
        )

        Student.objects.create(
            user=User.objects.get(username='6210612717'), std_id='6210612717', std_first='Hello', 
            std_last='World', b_date='2001-06-23', gender='Male', email='he@ex.com',
        )

        Course.objects.create(
            c_code='CN111', c_name='Course 1', semester=1, year='2022', 
            quota=2, status=True, )

    def test_index_user_is_authenticated(self):
        """ user is authenticated and user is superuser """

        self.client = Client()
        self.client.login(username='6210612716', password='lio12345', )
        response = self.client.get(reverse('users:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_user_is_not_superuser(self):
        """ user is authenticated and user is not superuser """

        student = Student.objects.get(std_id='6210612717')
        course = Course.objects.first()
        course.enrolled.add(student)

        self.client = Client()
        self.client.login(username='6210612717', password='lio12345', )
        response = self.client.get(reverse('users:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_user_is_not_authenticated(self):
        """ user is not authenticated """

        self.client = Client()
        response = self.client.get(reverse('users:index'))
        self.assertEqual(response.status_code, 302)

    def test_login_view_status_code(self):
        """ login view's status code is ok """

        self.client = Client()
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)

    def test_valid_password_login_view(self):
        """ login with valid password should return status code 302 """

        self.client = Client()
        response = self.client.post(reverse('users:login'), {'username': '6210612716', 'password': 'lio12345'})
        self.assertEqual(response.status_code, 302)

    def test_invalid_password_login_view(self):
        """ login with invalid password should return status code 200 """

        self.client = Client()
        response = self.client.post(reverse('users:login'), {'username': '6210612716', 'password': 'oli54321'})
        self.assertEqual(response.status_code, 200)

    def test_logout_view_status_code(self):
        """ logout view's status code is ok """

        self.client = Client()
        self.client.login(username='6210612716', password='lio12345')
        response = self.client.get(reverse('users:logout'))
        self.assertEqual(response.status_code, 200)
