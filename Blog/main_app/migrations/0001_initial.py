# Generated by Django 4.2.1 on 2023-05-30 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("Title", models.CharField(max_length=100)),
                ("Content", models.TextField()),
                ("is_published", models.BooleanField(default=False)),
                ("publish_date", models.DateField()),
            ],
        ),
    ]