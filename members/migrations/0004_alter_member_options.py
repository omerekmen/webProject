# Generated by Django 4.2.6 on 2023-11-06 18:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0003_alter_member_options_member_school"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="member",
            options={"verbose_name": "Üyeler", "verbose_name_plural": "Üyeler"},
        ),
    ]
