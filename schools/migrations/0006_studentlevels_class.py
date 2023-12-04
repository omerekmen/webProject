# Generated by Django 4.2.7 on 2023-12-04 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("schools", "0005_remove_schoolcampus_id_schoolcampus_capmus_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="StudentLevels",
            fields=[
                ("level_id", models.AutoField(primary_key=True, serialize=False)),
                ("LevelName", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Seviye",
                "verbose_name_plural": "Seviyeler",
            },
        ),
        migrations.CreateModel(
            name="Class",
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
                ("ClassName", models.CharField(max_length=255)),
                ("ClassDescription", models.TextField()),
                (
                    "LevelName",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schools.studentlevels",
                    ),
                ),
            ],
            options={
                "verbose_name": "Sınıf",
                "verbose_name_plural": "Sınıflar",
            },
        ),
    ]
