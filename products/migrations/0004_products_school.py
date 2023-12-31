# Generated by Django 4.2.6 on 2023-11-06 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("schools", "0002_alter_schools_options_and_more"),
        ("products", "0003_combinationproduct"),
    ]

    operations = [
        migrations.AddField(
            model_name="products",
            name="school",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="schools.schools",
            ),
        ),
    ]
