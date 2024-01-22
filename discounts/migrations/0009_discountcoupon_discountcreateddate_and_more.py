# Generated by Django 4.2.8 on 2023-12-15 15:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("discounts", "0008_alter_discountcoupon_discountminamount"),
    ]

    operations = [
        migrations.AddField(
            model_name="discountcoupon",
            name="discountCreatedDate",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="İndirim Oluşturulma Tarihi",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="discountcoupon",
            name="discountUpdatedDate",
            field=models.DateTimeField(
                auto_now=True, verbose_name="İndirim Güncellenme Tarihi"
            ),
        ),
        migrations.AddField(
            model_name="specialdiscount",
            name="discountCreatedDate",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="İndirim Oluşturulma Tarihi",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="specialdiscount",
            name="discountUpdatedDate",
            field=models.DateTimeField(
                auto_now=True, verbose_name="İndirim Güncellenme Tarihi"
            ),
        ),
    ]