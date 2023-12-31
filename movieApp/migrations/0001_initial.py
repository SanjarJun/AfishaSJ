# Generated by Django 4.2.6 on 2023-11-21 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Director",
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
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Director name"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Movie",
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
                ("title", models.CharField(max_length=255, verbose_name="Movie title")),
                (
                    "description",
                    models.CharField(max_length=255, verbose_name="Movie description"),
                ),
                (
                    "duration",
                    models.DecimalField(
                        decimal_places=2, max_digits=128, verbose_name="Movie duration"
                    ),
                ),
                (
                    "director",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="movieApp.director",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Review",
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
                ("text", models.CharField(max_length=255, verbose_name="Review text")),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="movieApp.movie"
                    ),
                ),
            ],
        ),
    ]
