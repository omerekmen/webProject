# Generated by Django 5.0 on 2024-02-12 13:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("schools", "__first__"),
        ("store", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Member",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("member_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "is_staff",
                    models.BooleanField(default=False, verbose_name="Staff Durumu"),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="E-Posta"
                    ),
                ),
                (
                    "phone_number",
                    models.IntegerField(blank=True, null=True, verbose_name="Telefon"),
                ),
                (
                    "username",
                    models.CharField(max_length=100, unique=True, verbose_name="TC No"),
                ),
                (
                    "first_name",
                    models.CharField(blank=True, max_length=150, verbose_name="Ad"),
                ),
                (
                    "last_name",
                    models.CharField(blank=True, max_length=150, verbose_name="Soyad"),
                ),
                (
                    "birth_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Doğum Tarihi"
                    ),
                ),
                (
                    "user_type",
                    models.CharField(
                        choices=[
                            ("Öğrenci", "Öğrenci"),
                            ("Mevcut Öğrenci", "Mevcut Öğrenci"),
                            ("Kurumsal", "Kurumsal"),
                            ("Kurum Admin", "Kurum Admin"),
                            ("SuperUser", "SuperUser"),
                        ],
                        default="Öğrenci",
                        max_length=100,
                        verbose_name="Kullanıcı Tipi",
                    ),
                ),
                (
                    "user_gender",
                    models.CharField(
                        choices=[("Erkek", "Erkek"), ("Kız", "Kız")],
                        max_length=100,
                        verbose_name="Cinsiyet",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Aktiflik Durumu"),
                ),
                (
                    "ip_address",
                    models.CharField(max_length=45, verbose_name="IP Adres"),
                ),
                (
                    "season",
                    models.IntegerField(
                        choices=[
                            (2000, 2000),
                            (2001, 2001),
                            (2002, 2002),
                            (2003, 2003),
                            (2004, 2004),
                            (2005, 2005),
                            (2006, 2006),
                            (2007, 2007),
                            (2008, 2008),
                            (2009, 2009),
                            (2010, 2010),
                            (2011, 2011),
                            (2012, 2012),
                            (2013, 2013),
                            (2014, 2014),
                            (2015, 2015),
                            (2016, 2016),
                            (2017, 2017),
                            (2018, 2018),
                            (2019, 2019),
                            (2020, 2020),
                            (2021, 2021),
                            (2022, 2022),
                            (2023, 2023),
                            (2024, 2024),
                            (2025, 2025),
                        ],
                        default=2024,
                        verbose_name="Sezon",
                    ),
                ),
                (
                    "registration_date",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="Kayıt Tarihi"
                    ),
                ),
                (
                    "campus_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schools.schoolcampus",
                    ),
                ),
                (
                    "class_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schools.class",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "level_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schools.studentlevels",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Üyeler",
                "verbose_name_plural": "Üyeler",
            },
        ),
        migrations.CreateModel(
            name="MemberAddress",
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
                    "AddressType",
                    models.CharField(
                        choices=[("Delivery", "Teslimat"), ("Invoice", "Fatura")],
                        max_length=100,
                    ),
                ),
                ("recipient_name", models.CharField(max_length=255)),
                ("recipient_lastname", models.CharField(max_length=255)),
                ("Country", models.CharField(default="Türkiye", max_length=100)),
                ("FullAddress", models.TextField()),
                ("PostalCode", models.PositiveIntegerField(blank=True, null=True)),
                ("PhoneNumber", models.IntegerField()),
                ("EMail", models.EmailField(max_length=254)),
                ("comp_name", models.CharField(blank=True, max_length=255, null=True)),
                ("tax_office", models.CharField(blank=True, max_length=255, null=True)),
                ("tax_no", models.PositiveBigIntegerField(blank=True, null=True)),
                ("CreatedAt", models.DateTimeField(auto_now_add=True)),
                ("UpdatedAt", models.DateTimeField(auto_now=True)),
                (
                    "City",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.city"
                    ),
                ),
                (
                    "District",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.district"
                    ),
                ),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]