# Generated by Django 4.2.3 on 2023-07-29 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Mechanic",
            fields=[
                ("mechanicID", models.AutoField(primary_key=True, serialize=False)),
                ("availability", models.BooleanField(default=True)),
            ],
        ),
    ]