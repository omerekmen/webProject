# Generated by Django 4.2.6 on 2023-11-03 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0011_remove_products_categorysizeid_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductPrices",
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
                ("SalePrice", models.DecimalField(decimal_places=2, max_digits=10)),
                ("StrikedPrice", models.IntegerField(blank=True, null=True)),
                ("DiscountRatio", models.IntegerField(blank=True, null=True)),
                ("DiscountPrice", models.IntegerField(blank=True, null=True)),
                ("DiscountType", models.IntegerField(blank=True, null=True)),
                (
                    "TaxPrice",
                    models.CharField(
                        blank=True,
                        choices=[(0, "0%"), (10, "10%"), (20, "20%")],
                        max_length=100,
                        null=True,
                    ),
                ),
                ("CombinePriceInfo", models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="products",
            name="PriceID",
        ),
        migrations.DeleteModel(
            name="ProductPrice",
        ),
        migrations.AddField(
            model_name="productprices",
            name="products",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="products.products"
            ),
        ),
    ]