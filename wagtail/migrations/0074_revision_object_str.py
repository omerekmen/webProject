# Generated by Django 4.0.4 on 2022-05-25 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0073_page_latest_revision"),
    ]

    operations = [
        migrations.AddField(
            model_name="revision",
            name="object_str",
            field=models.TextField(default=""),
        ),
    ]
