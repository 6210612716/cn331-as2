from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path('', views.course_view, name='course_view'),
    path('enroll', views.enroll, name='enroll'),
    path('cancel', views.cancel, name='cancel'),
    path('search', views.search, name='search'),
]