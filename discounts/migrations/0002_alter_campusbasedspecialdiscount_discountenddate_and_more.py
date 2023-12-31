# Generated by Django 4.2.8 on 2023-12-15 07:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("discounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="campusbasedspecialdiscount",
            name="discountEndDate",
            field=models.DateTimeField(
                blank=True,
                help_text="İndirim bitiş tarihi giriniz. Boş bırakırsanız indirim süresiz devam eder.",
                null=True,
                verbose_name="İndirim Bitiş Tarihi",
            ),
        ),
        migrations.AlterField(
            model_name="campusbasedspecialdiscount",
            name="discountStartDate",
            field=models.DateTimeField(
                blank=True,
                help_text="İndirim başlangıç tarihi giriniz. Boş bırakırsanız indirim anında aktif olur.",
                null=True,
                verbose_name="İndirim Başlangıç Tarihi",
            ),
        ),
    ]
