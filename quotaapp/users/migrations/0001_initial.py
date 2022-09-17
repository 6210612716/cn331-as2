# Generated by Django 4.1.1 on 2022-09-12 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
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
                ("sid", models.IntegerField()),
                ("sname", models.CharField(max_length=255)),
                ("slastname", models.CharField(max_length=255)),
                ("gender", models.CharField(max_length=64)),
                ("birth_date", models.CharField(max_length=10)),
                ("nationality", models.CharField(max_length=64)),
            ],
        ),
    ]