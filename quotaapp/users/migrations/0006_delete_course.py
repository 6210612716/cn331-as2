# Generated by Django 4.1.1 on 2022-09-16 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_remove_course_registered"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Course",
        ),
    ]