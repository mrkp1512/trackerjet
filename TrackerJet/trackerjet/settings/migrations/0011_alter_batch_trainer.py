# Generated by Django 4.2.1 on 2023-06-02 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("settings", "0010_rename_state_district_state_alter_batch_trainer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="batch",
            name="trainer",
            field=models.CharField(
                choices=[("1", "Neethu"), ("2", "Vrindha")], max_length=15
            ),
        ),
    ]