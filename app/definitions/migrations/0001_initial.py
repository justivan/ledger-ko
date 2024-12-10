# Generated by Django 5.1.3 on 2024-12-10 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Currency",
            fields=[
                (
                    "code",
                    models.CharField(max_length=3, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=120, unique=True)),
            ],
        ),
    ]