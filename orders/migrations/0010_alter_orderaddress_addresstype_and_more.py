# Generated by Django 4.2.8 on 2023-12-10 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0016_alter_combinationproduct_options_and_more"),
        ("orders", "0009_alter_orderproducts_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderaddress",
            name="AddressType",
            field=models.CharField(
                choices=[("Teslimat", "Teslimat"), ("Fatura", "Fatura")], max_length=100
            ),
        ),
        migrations.CreateModel(
            name="OrderCombinedProductChoice",
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
                (
                    "combination_product_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.combinationproduct",
                    ),
                ),
                (
                    "order_prod",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="orders.orderproducts",
                    ),
                ),
                (
                    "selected_product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.products",
                    ),
                ),
                (
                    "size_stock",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.sizebasedstocks",
                    ),
                ),
            ],
        ),
    ]
