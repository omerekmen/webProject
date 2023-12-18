# Generated by Django 4.2.8 on 2023-12-10 16:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0014_remove_temporderdetails_id_temporderdetails_member_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderpayment",
            name="CardAssociation",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="orderpayment",
            name="CardFamily",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="orderpayment",
            name="CardType",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="orderpayment",
            name="ConversationId",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="orderpayment",
            name="Currency",
            field=models.CharField(default="TRY", max_length=10),
        ),
        migrations.AddField(
            model_name="orderpayment",
            name="FraudStatus",
            field=models.CharField(
                choices=[
                    ("-1", "Yüksek Fraud Riski"),
                    ("0", "Fraud İhtimali"),
                    ("1", "Düşük Fraud Riski"),
                ],
                default="1",
                max_length=100,
            ),
        ),
        migrations.AddField(
            model_name="orderpayment",
            name="Installment",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="orderpayment",
            name="MerchantPayoutAmount",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AddField(
            model_name="orderpayment",
            name="PaidPrice",
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="orderpayment",
            name="PaymentId",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="orderpayment",
            name="PaymentProvider",
            field=models.CharField(
                choices=[("iyzico", "iyzico"), ("Diğer", "Diğer")],
                default="iyzico",
                max_length=100,
            ),
        ),
        migrations.AddField(
            model_name="orderpayment",
            name="PaymentStatus",
            field=models.CharField(
                choices=[
                    ("Ödeme Alındı", "Ödeme Alındı"),
                    ("Ödeme Alınmadı", "Ödeme Alınmadı"),
                ],
                default="Ödeme Alınmadı",
                max_length=100,
            ),
        ),
        migrations.AddField(
            model_name="orderpayment",
            name="Price",
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="orderpayment",
            name="iyziCommissionFee",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AddField(
            model_name="orderpayment",
            name="iyziCommissionRateAmount",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
    ]
