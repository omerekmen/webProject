# Generated by Django 4.2.6 on 2023-11-05 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_delete_combinationproduct_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CombinationProduct",
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
                ("CProductCategory", models.CharField(max_length=100)),
                (
                    "CombinProducts",
                    models.ManyToManyField(
                        blank=True,
                        related_name="combin_products",
                        to="products.products",
                        verbose_name="Ürün Seçimi",
                    ),
                ),
                (
                    "Product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.products",
                    ),
                ),
            ],
        ),
    ]