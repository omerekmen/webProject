# Generated by Django 4.2.7 on 2023-12-03 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0002_alter_district_options"),
        ("members", "0011_alter_memberaddress_addresstype"),
    ]

    operations = [
        migrations.AlterField(
            model_name="memberaddress",
            name="City",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="store.city"
            ),
        ),
        migrations.AlterField(
            model_name="memberaddress",
            name="District",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="store.district"
            ),
        ),
    ]
