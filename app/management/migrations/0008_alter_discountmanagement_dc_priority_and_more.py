# Generated by Django 4.2.7 on 2023-12-16 14:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("management", "0007_discountmanagement"),
    ]

    operations = [
        migrations.AlterField(
            model_name="discountmanagement",
            name="dc_priority",
            field=models.CharField(
                choices=[("Yüksek", "Yüksek"), ("Düşük", "Düşük")],
                default="Düşük",
                help_text="1: Yüksek Öncelik | 2: Düşük Öncelik",
                max_length=100,
                verbose_name="İndirim Kuponu Önceliği",
            ),
        ),
        migrations.AlterField(
            model_name="discountmanagement",
            name="sd_priority",
            field=models.CharField(
                choices=[("Yüksek", "Yüksek"), ("Düşük", "Düşük")],
                default="Yüksek",
                help_text="1: Yüksek Öncelik | 2: Düşük Öncelik",
                max_length=100,
                verbose_name="Özel İndirim Önceliği",
            ),
        ),
    ]