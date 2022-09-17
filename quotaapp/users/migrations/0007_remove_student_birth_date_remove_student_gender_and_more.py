# Generated by Django 4.1.1 on 2022-09-16 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("courses", "0037_delete_student"),
        ("users", "0006_delete_course"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="birth_date",
        ),
        migrations.RemoveField(
            model_name="student",
            name="gender",
        ),
        migrations.RemoveField(
            model_name="student",
            name="sid",
        ),
        migrations.RemoveField(
            model_name="student",
            name="slastname",
        ),
        migrations.RemoveField(
            model_name="student",
            name="sname",
        ),
        migrations.AddField(
            model_name="student",
            name="b_date",
            field=models.DateField(
                blank=True,
                help_text="format: YYYY-MM-DD",
                null=True,
                verbose_name="Birth Date",
            ),
        ),
        migrations.AddField(
            model_name="student",
            name="enrolled",
            field=models.ManyToManyField(
                blank=True, related_name="enrolled", to="courses.course"
            ),
        ),
        migrations.AddField(
            model_name="student",
            name="std_first",
            field=models.CharField(
                max_length=200, null=True, verbose_name="First Name"
            ),
        ),
        migrations.AddField(
            model_name="student",
            name="std_id",
            field=models.CharField(max_length=10, null=True, verbose_name="Student ID"),
        ),
        migrations.AddField(
            model_name="student",
            name="std_last",
            field=models.CharField(max_length=200, null=True, verbose_name="Last Name"),
        ),
        migrations.AddField(
            model_name="student",
            name="user",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="student_user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]