# Generated by Django 4.2.8 on 2023-12-28 13:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("support", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="supportticket",
            options={
                "ordering": ["-created_at"],
                "verbose_name": "Destek Talebi",
                "verbose_name_plural": "Destek Talepleri",
            },
        ),
        migrations.AlterField(
            model_name="supportticket",
            name="status",
            field=models.CharField(
                choices=[
                    ("OPEN", "Aktif"),
                    ("IN_PROGRESS", "Talebiniz İnceleniyor"),
                    ("CLOSED", "Çözüldü"),
                ],
                default="OPEN",
                max_length=20,
            ),
        ),
    ]