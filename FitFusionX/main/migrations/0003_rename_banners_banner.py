# Generated by Django 5.1 on 2024-08-20 05:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_banners_alter_service_title"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Banners",
            new_name="Banner",
        ),
    ]
