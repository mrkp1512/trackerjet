# Generated by Django 4.2.2 on 2023-06-19 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0012_student_batch'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
