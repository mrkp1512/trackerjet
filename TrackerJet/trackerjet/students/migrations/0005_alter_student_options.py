# Generated by Django 4.2.1 on 2023-05-26 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0004_alter_student_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="student", options={"verbose_name": "Students"},
        ),
    ]