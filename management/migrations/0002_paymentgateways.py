# Generated by Django 4.2.8 on 2023-12-14 12:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("management", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PaymentGateways",
            fields=[
                (
                    "pg_id",
                    models.BigAutoField(primary_key=True, serialize=False, unique=True),
                ),
                (
                    "payment_gateway",
                    models.CharField(
                        choices=[
                            ("iyzico", "IyziPay"),
                            ("param", "Param"),
                            ("ipara", "iPara"),
                        ],
                        max_length=255,
                        verbose_name="Ödeme Sağlayıcısı",
                    ),
                ),
                (
                    "payment_base_url",
                    models.CharField(max_length=1000, verbose_name="API Url"),
                ),
                (
                    "payment_api_key",
                    models.CharField(
                        blank=True, max_length=1000, null=True, verbose_name="API Key"
                    ),
                ),
                (
                    "payment_secret",
                    models.CharField(
                        blank=True,
                        max_length=1000,
                        null=True,
                        verbose_name="API Secret Key",
                    ),
                ),
                (
                    "payment_username",
                    models.CharField(
                        blank=True,
                        max_length=1000,
                        null=True,
                        verbose_name="API Client Username",
                    ),
                ),
                (
                    "payment_password",
                    models.CharField(
                        blank=True,
                        max_length=1000,
                        null=True,
                        verbose_name="API Client Password",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ödeme Sağlayıcı",
                "verbose_name_plural": "Ödeme Sağlayıcıları",
            },
        ),
    ]
