# Generated by Django 4.2.6 on 2023-11-03 16:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0008_sizebasedstocks"),
    ]

    operations = [
        migrations.RenameField(
            model_name="sizebasedstocks",
            old_name="product",
            new_name="products",
        ),
    ]
