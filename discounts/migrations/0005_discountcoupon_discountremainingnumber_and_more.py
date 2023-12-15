# Generated by Django 4.2.8 on 2023-12-15 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("schools", "0011_alter_schoolpopup_popup_title"),
        ("products", "0016_alter_combinationproduct_options_and_more"),
        ("discounts", "0004_rename_cbsd_id_specialdiscount_sd_id_discountcoupon"),
    ]

    operations = [
        migrations.AddField(
            model_name="discountcoupon",
            name="discountRemainingNumber",
            field=models.PositiveIntegerField(
                default=1,
                help_text="Kalan indirim adedi. Bu alan otomatik hesaplanacaktır Örnek: Bu indirim kodu 100 kere kullanılabilir. 50 kere kullanıldı. Kalan indirim adedi 50'dir.",
                verbose_name="Kalan İndirim Adedi",
            ),
        ),
        migrations.AddField(
            model_name="discountcoupon",
            name="discountTotalNumber",
            field=models.PositiveIntegerField(
                default=1,
                help_text="Toplam indirim adedi giriniz. Örnek: Bu indirim kodu toplamda 100 kere kullanılabilir.",
                verbose_name="Toplam İndirim Adedi",
            ),
        ),
        migrations.AlterField(
            model_name="discountcoupon",
            name="campus",
            field=models.ManyToManyField(
                blank=True,
                help_text="Kampüs bazlı indirim uygulanacak kampüsleri seçiniz.",
                related_name="discount_coupon",
                to="schools.schoolcampus",
                verbose_name="Kampüsler",
            ),
        ),
        migrations.AlterField(
            model_name="discountcoupon",
            name="discountPerPerson",
            field=models.PositiveIntegerField(
                default=1,
                help_text="Kişi başına indirim adedi giriniz. Örnek: A kişisi bu indirimden 1 kere yararlanabilir.",
                verbose_name="Kişi Başı İndirim Hakkı",
            ),
        ),
        migrations.AlterField(
            model_name="discountcoupon",
            name="member",
            field=models.ManyToManyField(
                blank=True,
                help_text="Öğrenci bazlı indirim uygulanacak öğrencileri seçiniz. (Öğrencinin bulunduğu kampüs Kampüsler alanında seçilmişse bu alan boş bırakılabilir.)",
                related_name="discount_coupon",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Öğrenciler",
            ),
        ),
        migrations.AlterField(
            model_name="discountcoupon",
            name="products",
            field=models.ManyToManyField(
                blank=True,
                help_text="Kampüs bazlı indirim uygulanacak ürünleri seçiniz.",
                related_name="discount_coupon",
                to="products.products",
                verbose_name="Ürünler",
            ),
        ),
        migrations.AlterField(
            model_name="discountcoupon",
            name="school",
            field=models.ForeignKey(
                help_text="Kampüs bazlı indirim uygulanacak okulu seçiniz.",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="discount_coupon",
                to="schools.schools",
                verbose_name="Okul",
            ),
        ),
        migrations.AlterField(
            model_name="specialdiscount",
            name="campus",
            field=models.ManyToManyField(
                blank=True,
                help_text="Kampüs bazlı indirim uygulanacak kampüsleri seçiniz.",
                related_name="special_discounts",
                to="schools.schoolcampus",
                verbose_name="Kampüsler",
            ),
        ),
        migrations.AlterField(
            model_name="specialdiscount",
            name="member",
            field=models.ManyToManyField(
                blank=True,
                help_text="Öğrenci bazlı indirim uygulanacak öğrencileri seçiniz. (Öğrencinin bulunduğu kampüs Kampüsler alanında seçilmişse bu alan boş bırakılabilir.)",
                related_name="special_discounts",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Öğrenciler",
            ),
        ),
        migrations.AlterField(
            model_name="specialdiscount",
            name="products",
            field=models.ManyToManyField(
                blank=True,
                help_text="Kampüs bazlı indirim uygulanacak ürünleri seçiniz.",
                related_name="special_discounts",
                to="products.products",
                verbose_name="Ürünler",
            ),
        ),
        migrations.AlterField(
            model_name="specialdiscount",
            name="school",
            field=models.ForeignKey(
                help_text="Kampüs bazlı indirim uygulanacak okulu seçiniz.",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="special_discounts",
                to="schools.schools",
                verbose_name="Okul",
            ),
        ),
    ]