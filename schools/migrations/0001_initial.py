# Generated by Django 4.2.6 on 2023-11-06 11:10

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import schools.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Schools",
            fields=[
                ("school_id", models.AutoField(primary_key=True, serialize=False)),
                ("school_name", models.CharField(max_length=255)),
                ("school_phone", models.CharField(max_length=15)),
                ("school_subdomain", models.CharField(max_length=15)),
            ],
            options={
                "verbose_name": "Okullar",
                "verbose_name_plural": "Okullar",
            },
        ),
        migrations.CreateModel(
            name="SchoolSlider",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "slider_image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=schools.models.upload_location_settings,
                    ),
                ),
                (
                    "slider_title",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "slider_description",
                    ckeditor.fields.RichTextField(blank=True, null=True),
                ),
                (
                    "school",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schools.schools",
                    ),
                ),
            ],
            options={
                "verbose_name": "Okul Sliderları",
                "verbose_name_plural": "Okul Sliderları",
            },
        ),
        migrations.CreateModel(
            name="SchoolSiteSettings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "school_intro_image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=schools.models.upload_location_settings,
                    ),
                ),
                (
                    "school_logo_header",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=schools.models.upload_location_settings,
                    ),
                ),
                ("school_header_title", models.CharField(max_length=255)),
                (
                    "school_logo_footer",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=schools.models.upload_location_settings,
                    ),
                ),
                ("school_footer_title", models.CharField(max_length=255)),
                ("school_footer_adress", models.TextField(blank=True, null=True)),
                ("school_shop_adress", models.TextField(blank=True, null=True)),
                (
                    "school",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schools.schools",
                    ),
                ),
            ],
            options={
                "verbose_name": "Okul Ayarları",
                "verbose_name_plural": "Okul Ayarları",
            },
        ),
        migrations.CreateModel(
            name="SchoolPopup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "popup_page",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("intro", "Giriş Popup"),
                            ("index", "Anasayfa Popup"),
                            ("product", "Ürün Detay Popup"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                ("popup_title", models.CharField(blank=True, max_length=15, null=True)),
                ("popup_content", ckeditor.fields.RichTextField(blank=True, null=True)),
                ("popup_status", models.BooleanField(default=True)),
                (
                    "school",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schools.schools",
                    ),
                ),
            ],
            options={
                "verbose_name": "Popup Ayarları",
                "verbose_name_plural": "Popup Ayarları",
            },
        ),
        migrations.CreateModel(
            name="SchoolPages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("page_title", models.CharField(max_length=255)),
                (
                    "page_category",
                    models.CharField(
                        choices=[("pages", "Sayfalar"), ("contracts", "Sözleşmeler")],
                        max_length=50,
                    ),
                ),
                ("page_url", models.SlugField(max_length=255, unique=True)),
                ("footer_visibility", models.BooleanField(default=True)),
                ("page_content", ckeditor.fields.RichTextField()),
                (
                    "school",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schools.schools",
                    ),
                ),
            ],
            options={
                "verbose_name": "Okul Sayfaları",
                "verbose_name_plural": "Okul Sayfaları",
            },
        ),
        migrations.CreateModel(
            name="SchoolCampus",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("campus_name", models.CharField(max_length=255)),
                ("campus_phone", models.CharField(max_length=15)),
                ("campus_email", models.EmailField(max_length=255)),
                ("franchise_state", models.BooleanField()),
                (
                    "City",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="İl"
                    ),
                ),
                (
                    "District",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="İlçe"
                    ),
                ),
                (
                    "FullAddress",
                    models.TextField(blank=True, null=True, verbose_name="Tam Adres"),
                ),
                (
                    "PostalCode",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Posta Kodu"
                    ),
                ),
                (
                    "AuthorizedFirstName",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Yetkili Adı"
                    ),
                ),
                (
                    "AuthorizedLastName",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Yetkili Soyadı",
                    ),
                ),
                (
                    "AuthorizedPhone",
                    models.CharField(
                        blank=True,
                        max_length=15,
                        null=True,
                        verbose_name="Yetkili Telefon",
                    ),
                ),
                (
                    "AuthorizedEmail",
                    models.EmailField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Yetkili E-mail",
                    ),
                ),
                (
                    "school",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schools.schools",
                    ),
                ),
            ],
            options={
                "verbose_name": "Kampüsler",
                "verbose_name_plural": "Kampüsler",
            },
        ),
    ]
