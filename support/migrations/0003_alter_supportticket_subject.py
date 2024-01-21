# Generated by Django 5.0 on 2024-01-21 15:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("support", "0002_alter_supportticket_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="supportticket",
            name="subject",
            field=models.CharField(
                choices=[
                    ("Degisim", "Kıyafet/Değişim"),
                    ("Iade", "Kıyafet/İade"),
                    ("Iptal", "Kıyafet/İptal"),
                    ("Fatura", "Kıyafet/Fatura"),
                    ("Urun", "Kıyafet/Ürün"),
                    ("Siparis", "Kıyafet/Sipariş"),
                    ("Web", "Kıyafet/Web"),
                    ("Kargo", "Kıyafet/Kargo"),
                    ("Teslimat", "Kıyafet/Teslimat"),
                    ("Odeme", "Kıyafet/Ödeme"),
                    ("HataliUrun", "Kıyafet/Hatalı Ürün"),
                    ("EskiUrun", "Kıyafet/Eski Ürün"),
                    ("Kargolama", "Kitap/Kargolama"),
                    ("SipIptal", "Kitap/Sipariş İptal"),
                    ("KitapDegisim", "Kitap/Değişim"),
                    ("KitapIade", "Kitap/İade"),
                    ("KitapIptal", "Kitap/İptal"),
                    ("KitapKargo", "Kitap/Kargo"),
                    ("KitapTeslimat", "Kitap/Teslimat"),
                    ("KitapHataliUrun", "Kitap/Hatalı Ürün"),
                    ("KitapEksikUrun", "Kitap/Eksik Ürün"),
                ],
                max_length=200,
            ),
        ),
    ]
