# Generated by Django 4.1.1 on 2022-09-15 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0014_alter_course_semester_alter_course_year_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="course",
            name="year",
        ),
    ]