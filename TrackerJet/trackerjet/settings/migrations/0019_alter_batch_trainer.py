# Generated by Django 4.2.1 on 2023-06-05 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("settings", "0018_alter_batch_trainer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="batch",
            name="trainer",
            field=models.CharField(
                choices=[("2", "Vrindha"), ("1", "Neethu")], max_length=15
            ),
        ),
    ]
