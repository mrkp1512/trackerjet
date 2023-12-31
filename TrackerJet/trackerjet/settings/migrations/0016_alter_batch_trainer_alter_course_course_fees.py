# Generated by Django 4.2.1 on 2023-06-03 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("settings", "0015_alter_batch_trainer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="batch",
            name="trainer",
            field=models.CharField(
                choices=[("1", "Neethu"), ("2", "Vrindha")], max_length=15
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="course_fees",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="settings.course_fees",
            ),
        ),
    ]
