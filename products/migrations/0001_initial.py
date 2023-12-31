# Generated by Django 4.2.6 on 2023-11-04 22:08

from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CombinationProduct",
            fields=[
                ("CProductID", models.AutoField(primary_key=True, serialize=False)),
                ("SProductInfo", models.JSONField(blank=True, null=True)),
                ("CProductQuantity", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="ProductCategory",
            fields=[
                (
                    "ProductCategoryID",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("CategoryName", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="ProductCategorySizes",
            fields=[
                ("CategorySizeID", models.AutoField(primary_key=True, serialize=False)),
                ("ProductSize", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "Ürün Bedenleri",
                "verbose_name_plural": "Ürün Bedenleri",
                "ordering": ["ProductSize"],
            },
        ),
        migrations.CreateModel(
            name="Products",
            fields=[
                (
                    "ProductID",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="Ürün ID"
                    ),
                ),
                (
                    "product_type",
                    models.CharField(
                        choices=[
                            ("Set", "Set"),
                            ("Kombin", "Kombin"),
                            ("Tekil", "Tekil"),
                        ],
                        default="Tekil",
                        max_length=100,
                        verbose_name="Ürün Türü",
                    ),
                ),
                (
                    "product_production_name",
                    models.CharField(max_length=255, verbose_name="Ürün Üretim Adı"),
                ),
                (
                    "product_name",
                    models.CharField(max_length=255, verbose_name="Ürün Adı"),
                ),
                (
                    "product_web_name",
                    models.CharField(max_length=255, verbose_name="Ürün Web Adı"),
                ),
                (
                    "product_production_date",
                    models.DateField(verbose_name="Üretim Tarihi"),
                ),
                (
                    "model_code",
                    models.CharField(max_length=100, verbose_name="Model Kodu"),
                ),
                (
                    "product_color",
                    models.CharField(max_length=100, verbose_name="Ürün Rengi"),
                ),
                ("book_type", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "product_state",
                    models.CharField(
                        choices=[("Aktif", "Aktif"), ("Pasif", "Pasif")],
                        default="Aktif",
                        max_length=100,
                        verbose_name="Ürün Durumu",
                    ),
                ),
                (
                    "product_genre",
                    models.CharField(
                        choices=[
                            ("Kız", "Kız"),
                            ("Erkek", "Erkek"),
                            ("Unisex", "Unisex"),
                        ],
                        max_length=100,
                        verbose_name="Cinsiyet",
                    ),
                ),
                (
                    "product_class",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "product_level",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("product_measure_unit", models.CharField(max_length=100)),
                (
                    "product_created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Oluşturulma Tarihi"
                    ),
                ),
                (
                    "product_last_update",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Güncelleme Tarihi"
                    ),
                ),
                (
                    "season",
                    models.IntegerField(
                        choices=[
                            (2000, 2000),
                            (2001, 2001),
                            (2002, 2002),
                            (2003, 2003),
                            (2004, 2004),
                            (2005, 2005),
                            (2006, 2006),
                            (2007, 2007),
                            (2008, 2008),
                            (2009, 2009),
                            (2010, 2010),
                            (2011, 2011),
                            (2012, 2012),
                            (2013, 2013),
                            (2014, 2014),
                            (2015, 2015),
                            (2016, 2016),
                            (2017, 2017),
                            (2018, 2018),
                            (2019, 2019),
                            (2020, 2020),
                            (2021, 2021),
                            (2022, 2022),
                            (2023, 2023),
                            (2024, 2024),
                        ],
                        default=2023,
                        verbose_name="Sezon",
                    ),
                ),
                ("product_change_limit", models.JSONField(blank=True, null=True)),
                ("school_management", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "Ürünler",
                "verbose_name_plural": "Ürünler",
                "ordering": ["-product_created_at"],
                "permissions": [
                    ("view_bk_products", "Can view bkAdmin products"),
                    ("edit_bk_products", "Can edit bkAdmin products"),
                    ("view_girne_products", "Can view girneAdmin products"),
                    ("edit_girne_products", "Can edit girneAdmin products"),
                ],
            },
        ),
        migrations.CreateModel(
            name="SetProduct",
            fields=[
                ("SetID", models.AutoField(primary_key=True, serialize=False)),
                ("SProductInfo", models.JSONField()),
                ("SProductQuantity", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="SizeBasedStocks",
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
                ("SKU_code", models.CharField(max_length=100)),
                ("barcode", models.CharField(max_length=100)),
                ("real_stock", models.PositiveIntegerField(default=0)),
                ("sale_stock", models.PositiveIntegerField(default=0)),
                ("reserved_stock", models.PositiveIntegerField(default=0)),
                ("accept_stock", models.PositiveIntegerField(default=0)),
                ("return_stock", models.PositiveIntegerField(default=0)),
                ("cancel_stock", models.PositiveIntegerField(default=0)),
                ("preproduction_stock", models.PositiveIntegerField(default=0)),
                (
                    "products",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.products",
                    ),
                ),
                (
                    "size",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.productcategorysizes",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ürün Beden & Stok",
                "verbose_name_plural": "Ürün Beden & Stok",
            },
        ),
        migrations.CreateModel(
            name="ProductSubCategory",
            fields=[
                (
                    "ProductSubCategoryID",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("SubCategoryName", models.CharField(max_length=255)),
                (
                    "ProductCategory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.productcategory",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="products",
            name="ProductSubCategoryID",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="products.productsubcategory",
            ),
        ),
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
                (
                    "StrikedPrice",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
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
                (
                    "products",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.products",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ürün Fiyat",
                "verbose_name_plural": "Ürün Fiyat",
            },
        ),
        migrations.CreateModel(
            name="ProductImages",
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
                    "product_image",
                    models.FileField(
                        blank=True, null=True, upload_to=products.models.upload_location
                    ),
                ),
                (
                    "products",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.products",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ürün Görselleri",
                "verbose_name_plural": "Ürün Görselleri",
            },
        ),
        migrations.CreateModel(
            name="ProductDetails",
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
                ("product_detail", models.CharField(max_length=255)),
                ("product_info", models.CharField(max_length=255)),
                ("product_size_table", models.CharField(max_length=255)),
                ("product_suggestions", models.CharField(max_length=255)),
                ("product_quality", models.CharField(max_length=255)),
                ("product_find_size", models.CharField(max_length=255)),
                ("product_measure", models.CharField(max_length=255)),
                ("product_video", models.CharField(max_length=255)),
                (
                    "products",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.products",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ürün Detayları",
                "verbose_name_plural": "Ürün Detayları",
            },
        ),
    ]
