# Generated by Django 4.1.1 on 2022-09-15 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="c_semester",
            field=models.ForeignKey(
                choices=[("one", "1"), ("two", "2"), ("summer", "3")],
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="c_semester",
                to="courses.semester",
                verbose_name="Semester",
            ),
        ),
    ]