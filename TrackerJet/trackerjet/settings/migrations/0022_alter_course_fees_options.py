# Generated by Django 4.2.1 on 2023-06-05 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("settings", "0021_remove_batch_trainer_course_trainer"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="course_fees",
            options={
                "verbose_name": "Course Fee",
                "verbose_name_plural": "Course Fees",
            },
        ),
    ]