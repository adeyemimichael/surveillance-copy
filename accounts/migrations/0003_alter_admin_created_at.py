# Generated by Django 4.2.11 on 2024-05-04 10:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_alter_admin_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="admin",
            name="created_at",
            field=models.DateTimeField(),
        ),
    ]
