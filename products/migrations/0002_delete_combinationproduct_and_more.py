# Generated by Django 4.2.6 on 2023-11-05 22:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CombinationProduct",
        ),
        migrations.AlterModelOptions(
            name="productcategory",
            options={
                "verbose_name": "Ürün Kategorileri",
                "verbose_name_plural": "Ürün Kategorileri",
            },
        ),
        migrations.AlterModelOptions(
            name="productcategorysizes",
            options={
                "ordering": ["CategorySizeID"],
                "verbose_name": "Ürün Bedenleri",
                "verbose_name_plural": "Ürün Bedenleri",
            },
        ),
        migrations.AlterModelOptions(
            name="productsubcategory",
            options={
                "verbose_name": "Ürün Alt Kategorileri",
                "verbose_name_plural": "Ürün Alt Kategorileri",
            },
        ),
        migrations.AlterField(
            model_name="productcategory",
            name="CategoryName",
            field=models.CharField(max_length=255, verbose_name="Kategori Adı"),
        ),
    ]
