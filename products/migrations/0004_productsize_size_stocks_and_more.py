# Generated by Django 4.2.6 on 2023-10-25 21:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0003_productsize_alter_productprice_taxprice_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="productsize",
            name="size_stocks",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="productprice",
            name="DiscountPrice",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="productprice",
            name="DiscountRatio",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="productprice",
            name="StrikedPrice",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]