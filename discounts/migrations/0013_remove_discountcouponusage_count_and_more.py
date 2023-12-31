# Generated by Django 4.2.7 on 2023-12-16 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("discounts", "0012_specialdiscountusage"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="discountcouponusage",
            name="count",
        ),
        migrations.RemoveField(
            model_name="specialdiscountusage",
            name="count",
        ),
        migrations.AddField(
            model_name="discountcouponusage",
            name="count_usage",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Kullanım Sayısı"
            ),
        ),
        migrations.AddField(
            model_name="specialdiscountusage",
            name="count_usage",
            field=models.PositiveIntegerField(
                default=0, verbose_name="Kullanım Sayısı"
            ),
        ),
        migrations.AlterField(
            model_name="discountcouponusage",
            name="discount",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="discounts.discountcoupon",
                verbose_name="Kullanılan Kod",
            ),
        ),
        migrations.AlterField(
            model_name="discountcouponusage",
            name="member",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Kullanan Kişi",
            ),
        ),
        migrations.AlterField(
            model_name="specialdiscountusage",
            name="discount",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="discounts.specialdiscount",
                verbose_name="Kullanılan İndirim",
            ),
        ),
        migrations.AlterField(
            model_name="specialdiscountusage",
            name="member",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Kullanan Kişi",
            ),
        ),
    ]
