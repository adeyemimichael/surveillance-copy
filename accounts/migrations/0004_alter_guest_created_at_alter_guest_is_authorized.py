# Generated by Django 4.2.11 on 2024-05-18 11:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_alter_admin_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="guest",
            name="created_at",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="guest",
            name="is_authorized",
            field=models.BooleanField(),
        ),
    ]
