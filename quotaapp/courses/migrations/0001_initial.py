# Generated by Django 4.1.1 on 2022-09-15 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "c_name",
                    models.CharField(max_length=200, verbose_name="Course Name"),
                ),
                ("year", models.IntegerField(verbose_name="Year")),
                ("quota", models.IntegerField(default=0)),
                (
                    "status",
                    models.CharField(
                        choices=[("open", "Open"), ("close", "Close")], max_length=50
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Semester",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("std_id", models.IntegerField(unique=True, verbose_name="Student ID")),
                (
                    "std_first",
                    models.CharField(max_length=200, verbose_name="First Name"),
                ),
                (
                    "std_last",
                    models.CharField(max_length=200, verbose_name="Last Name"),
                ),
                ("b_date", models.DateField(blank=True, verbose_name="Birth Date")),
            ],
        ),
        migrations.CreateModel(
            name="Enroll",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "course",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="courses.course",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="courses.student",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="course",
            name="c_semester",
            field=models.ForeignKey(
                choices=[("one", "1"), ("two", "2"), ("summer", "3")],
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="c_semester",
                to="courses.semester",
            ),
        ),
    ]
