# Generated by Django 4.2.6 on 2023-10-25 21:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_alter_combinationproduct_sproductinfo_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductSize",
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
                ("size_name", models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name="productprice",
            name="TaxPrice",
            field=models.CharField(
                blank=True,
                choices=[(0, "0%"), (10, "10%"), (20, "20%")],
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="productstock",
            name="AcceptStock",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="productstock",
            name="CancelStock",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="productstock",
            name="PreproductionStock",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="productstock",
            name="RealStock",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="productstock",
            name="ReservedStock",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="productstock",
            name="ReturnStock",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="productstock",
            name="SaleStock",
            field=models.PositiveIntegerField(),
        ),
        migrations.AddField(
            model_name="products",
            name="product_sizes",
            field=models.ManyToManyField(to="products.productsize"),
        ),
    ]