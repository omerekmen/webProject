# Generated by Django 4.2.7 on 2023-12-03 13:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("store", "0002_alter_district_options"),
        ("orders", "0003_alter_orderproducts_quantity"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="orderaddress",
            name="BuyerLastName",
        ),
        migrations.RemoveField(
            model_name="orderaddress",
            name="BuyerName",
        ),
        migrations.AddField(
            model_name="orderaddress",
            name="Country",
            field=models.CharField(default="Türkiye", max_length=100),
        ),
        migrations.AddField(
            model_name="orderaddress",
            name="comp_name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="orderaddress",
            name="recipient_lastname",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="orderaddress",
            name="recipient_name",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="orderaddress",
            name="tax_no",
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="orderaddress",
            name="tax_office",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="orderaddress",
            name="AddressType",
            field=models.CharField(
                choices=[("Delivery", "Teslimat"), ("Invoice", "Fatura")],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="orderaddress",
            name="City",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="store.city"
            ),
        ),
        migrations.AlterField(
            model_name="orderaddress",
            name="District",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="store.district"
            ),
        ),
        migrations.AlterField(
            model_name="orderaddress",
            name="FullAddress",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="orderaddress",
            name="PostalCode",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="orders",
            name="Member",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="TC No",
            ),
        ),
        migrations.AlterField(
            model_name="orders",
            name="OrderID",
            field=models.SlugField(
                editable=False,
                max_length=10,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
