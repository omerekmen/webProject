# Generated by Django 4.2.7 on 2023-12-16 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("discounts", "0013_remove_discountcouponusage_count_and_more"),
        ("cart", "0007_alter_cart_specialdiscountstatus"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="SpecialDiscountApplied",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="discounts.specialdiscount",
                verbose_name="Uygulanan İndirim",
            ),
        ),
    ]
