# Generated by Django 4.2.7 on 2023-11-07 20:04

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0009_productdetails_product_short_desc_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productdetails",
            name="product_detail",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="productdetails",
            name="product_find_size",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="productdetails",
            name="product_info",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="productdetails",
            name="product_measure",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="productdetails",
            name="product_quality",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="productdetails",
            name="product_short_desc",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="productdetails",
            name="product_size_table",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="productdetails",
            name="product_suggestions",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="productdetails",
            name="product_video",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
