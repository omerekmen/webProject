# Generated by Django 4.2.8 on 2023-12-15 15:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("discounts", "0006_alter_discountcoupon_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="discountcoupon",
            name="products",
        ),
    ]
