# Generated by Django 4.2.8 on 2023-12-14 12:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("management", "0002_paymentgateways"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailsettings",
            name="mail_port",
            field=models.IntegerField(max_length=255, verbose_name="Mail Port"),
        ),
    ]