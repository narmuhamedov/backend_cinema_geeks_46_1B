# Generated by Django 5.1.2 on 2024-11-08 11:41

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_page", "0003_alter_films_options_films_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="ReviewFilm",
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
                ("created_at", models.DateField(auto_now_add=True)),
                (
                    "description",
                    models.TextField(verbose_name="Оставьте отзыв о фильме"),
                ),
                (
                    "mark",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                        verbose_name="Укажите оценку от 1 до 5",
                    ),
                ),
                (
                    "review_films",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="review_films",
                        to="main_page.films",
                    ),
                ),
            ],
            options={
                "verbose_name": "комментарий",
                "verbose_name_plural": "комментарии",
            },
        ),
    ]
