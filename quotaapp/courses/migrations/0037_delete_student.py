# Generated by Django 4.1.1 on 2022-09-16 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0036_alter_student_b_date_alter_student_std_first_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Student",
        ),
    ]
