# Generated by Django 5.1.2 on 2024-11-19 12:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("parsing_rezka", "0002_alter_rezka_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rezka",
            name="image",
            field=models.ImageField(null=True, upload_to=""),
        ),
    ]
