# Generated by Django 5.1 on 2024-08-22 10:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0017_subplan_max_member"),
    ]

    operations = [
        migrations.CreateModel(
            name="PlanDiscount",
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
                ("total_months", models.IntegerField()),
                ("total_discount", models.IntegerField()),
                (
                    "subplan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.subplan"
                    ),
                ),
            ],
        ),
    ]
