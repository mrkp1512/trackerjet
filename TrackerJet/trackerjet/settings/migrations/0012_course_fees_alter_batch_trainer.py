# Generated by Django 4.2.1 on 2023-06-03 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("settings", "0011_alter_batch_trainer"),
    ]

    operations = [
        migrations.CreateModel(
            name="Course_fees",
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
                ("fees_type", models.CharField(max_length=50)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=8)),
                ("tax", models.DecimalField(decimal_places=2, max_digits=8)),
                ("installment_period", models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name="batch",
            name="trainer",
            field=models.CharField(
                choices=[("2", "Vrindha"), ("1", "Neethu")], max_length=15
            ),
        ),
    ]
