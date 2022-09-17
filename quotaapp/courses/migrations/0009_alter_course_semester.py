# Generated by Django 4.1.1 on 2022-09-15 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0008_rename_c_semester_course_semester"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="semester",
            field=models.OneToOneField(
                choices=[("one", "1"), ("two", "2"), ("summer", "3")],
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="c_semester",
                to="courses.semester",
                verbose_name="Semester",
            ),
        ),
    ]