# Generated by Django 4.2.7 on 2023-11-12 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0014_remove_productcategory_school_and_more"),
        ("cart", "0003_remove_cart_id_remove_cart_product_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="cartitems",
            name="size_stock",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="products.sizebasedstocks",
            ),
        ),
        migrations.AddField(
            model_name="combinedproductchoice",
            name="size_stock",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="products.sizebasedstocks",
            ),
        ),
    ]