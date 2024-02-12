# Generated by Django 5.0 on 2024-02-12 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Manufacturer",
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
                ("name", models.CharField(max_length=50, verbose_name="Üretici Adı")),
                ("address", models.CharField(max_length=200, verbose_name="Adres")),
                (
                    "tax_no",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="Vergi No"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=50, null=True, verbose_name="E-posta"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="Telefon"
                    ),
                ),
                (
                    "fax",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="Faks"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Oluşturulma Tarihi"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Güncellenme Tarihi"
                    ),
                ),
            ],
            options={
                "verbose_name": "Üretici",
                "verbose_name_plural": "Üreticiler",
            },
        ),
        migrations.CreateModel(
            name="Supplier",
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
                ("name", models.CharField(max_length=50, verbose_name="Tedarikçi Adı")),
                ("address", models.CharField(max_length=200, verbose_name="Adres")),
                (
                    "tax_no",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="Vergi No"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=50, null=True, verbose_name="E-posta"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="Telefon"
                    ),
                ),
                (
                    "fax",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="Faks"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Oluşturulma Tarihi"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Güncellenme Tarihi"
                    ),
                ),
            ],
            options={
                "verbose_name": "Tedarikçi",
                "verbose_name_plural": "Tedarikçiler",
            },
        ),
        migrations.CreateModel(
            name="Warehouse",
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
                ("name", models.CharField(max_length=50, verbose_name="Depo Adı")),
                ("address", models.CharField(max_length=200, verbose_name="Adres")),
                ("phone", models.CharField(max_length=20, verbose_name="Telefon")),
                ("fax", models.CharField(max_length=20, verbose_name="Faks")),
            ],
            options={
                "verbose_name": "Depo",
                "verbose_name_plural": "Depolar",
            },
        ),
        migrations.CreateModel(
            name="Shipment",
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
                ("name", models.CharField(max_length=50, verbose_name="Sevkiyat Adı")),
                (
                    "vehicle_type",
                    models.CharField(
                        choices=[
                            ("Tır", "Tır"),
                            ("Kamyon", "Kamyon"),
                            ("Kargo", "Kargo"),
                        ],
                        max_length=50,
                        verbose_name="Araç Tipi",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Oluşturulma Tarihi"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Güncellenme Tarihi"
                    ),
                ),
                (
                    "manufacturer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="warehouse.manufacturer",
                        verbose_name="Üretici",
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="warehouse.supplier",
                        verbose_name="Tedarikçi",
                    ),
                ),
                (
                    "warehouse",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="warehouse.warehouse",
                        verbose_name="Depo",
                    ),
                ),
            ],
            options={
                "verbose_name": "Sevkiyat",
                "verbose_name_plural": "Sevkiyatlar",
            },
        ),
        migrations.CreateModel(
            name="Waybill",
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
                    "waybill_no",
                    models.CharField(max_length=50, verbose_name="İrsaliye No"),
                ),
                ("waybill_date", models.DateField(verbose_name="İrsaliye Tarihi")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Oluşturulma Tarihi"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Güncellenme Tarihi"
                    ),
                ),
                (
                    "shipment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="warehouse.shipment",
                        verbose_name="Sevkiyat",
                    ),
                ),
            ],
            options={
                "verbose_name": "İrsaliye",
                "verbose_name_plural": "İrsaliyeler",
            },
        ),
        migrations.CreateModel(
            name="WaybillProduct",
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
                    "quantity",
                    models.PositiveIntegerField(verbose_name="Beklenen Miktar"),
                ),
                (
                    "act_quantity",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="Sayılan Miktar"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.products",
                        verbose_name="Ürün",
                    ),
                ),
                (
                    "product_size",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.productcategorysizes",
                        verbose_name="Ürün Boyutu",
                    ),
                ),
                (
                    "waybill",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="warehouse.waybill",
                        verbose_name="İrsaliye",
                    ),
                ),
            ],
            options={
                "verbose_name": "İrsaliye Kontrol",
                "verbose_name_plural": "İrsaliye Kontrolleri",
            },
        ),
        migrations.CreateModel(
            name="WarehouseStock",
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
                ("stock", models.PositiveIntegerField(verbose_name="Stok")),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.products",
                        verbose_name="Ürün",
                    ),
                ),
                (
                    "product_size",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.productcategorysizes",
                        verbose_name="Ürün Boyutu",
                    ),
                ),
                (
                    "warehouse",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="warehouse.warehouse",
                        verbose_name="Depo",
                    ),
                ),
            ],
            options={
                "verbose_name": "Depo Stok",
                "verbose_name_plural": "Depo Stokları",
                "unique_together": {("warehouse", "product")},
            },
        ),
    ]
