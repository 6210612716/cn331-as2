# Generated by Django 4.1.1 on 2022-09-16 06:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("courses", "0029_alter_quota_student"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="status",
            field=models.BooleanField(
                default=True,
                help_text="Check = Open, Uncheck = Close",
                verbose_name="Course Status",
            ),
        ),
        migrations.AlterField(
            model_name="quota",
            name="student",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="students",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
