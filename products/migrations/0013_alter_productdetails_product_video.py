# Generated by Django 4.2.7 on 2023-11-11 17:19

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0012_productcategory_school"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productdetails",
            name="product_video",
            field=ckeditor_uploader.fields.RichTextUploadingField(
                blank=True, null=True
            ),
        ),
    ]
