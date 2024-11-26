# Generated by Django 5.1.2 on 2024-11-05 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Films",
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
                    "image",
                    models.ImageField(
                        upload_to="film/", verbose_name="загрузите картинку"
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=100, verbose_name="Укажите описание фильма"
                    ),
                ),
                ("price", models.FloatField(verbose_name="Укажите цену")),
                ("start_film", models.DateField(verbose_name="укажите дату выхода")),
                (
                    "genre",
                    models.CharField(
                        choices=[
                            ("Ужасы", "Ужасы"),
                            ("Комедия", "Комедия"),
                            ("Боевик", "Боевик"),
                        ],
                        default="Комедия",
                        max_length=100,
                        verbose_name="Укажите жанр",
                    ),
                ),
                (
                    "time_end",
                    models.TimeField(
                        verbose_name="Укажите время продолжительности фильма"
                    ),
                ),
                (
                    "director",
                    models.CharField(max_length=30, verbose_name="Укажите режиссёра"),
                ),
                (
                    "trailer",
                    models.URLField(verbose_name="Укажите ссылку трейлера с youtube"),
                ),
            ],
        ),
    ]
