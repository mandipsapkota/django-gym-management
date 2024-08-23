# Generated by Django 5.1 on 2024-08-23 03:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0019_subscriber"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="subscriber",
            name="plan",
        ),
        migrations.RemoveField(
            model_name="subscriber",
            name="price",
        ),
        migrations.AddField(
            model_name="subscriber",
            name="address",
            field=models.TextField(default="Default"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="subscriber",
            name="img",
            field=models.ImageField(default="Default value", upload_to="subscribers/"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="subscriber",
            name="mobile",
            field=models.CharField(default=9800000000, max_length=20),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="Subscription",
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
                ("price", models.CharField(max_length=50)),
                (
                    "plan",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.subplan",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
