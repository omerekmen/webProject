# Generated by Django 4.2.7 on 2023-12-16 21:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("discounts", "0013_remove_discountcouponusage_count_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="specialdiscountusage",
            old_name="dcu_id",
            new_name="sdu_id",
        ),
    ]
