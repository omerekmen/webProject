# Generated by Django 4.2.6 on 2023-11-06 11:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_products_school"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="products",
            name="school_management",
        ),
    ]
