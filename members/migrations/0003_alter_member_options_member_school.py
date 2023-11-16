# Generated by Django 4.2.6 on 2023-11-06 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("schools", "0002_alter_schools_options_and_more"),
        (
            "members",
            "0002_remove_studentlevels_campusid_alter_member_campus_id_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="member",
            options={
                "permissions": [
                    ("view_bk_members", "Can view bkAdmin members"),
                    ("edit_bk_members", "Can edit bkAdmin members"),
                    ("view_girne_members", "Can view girneAdmin members"),
                    ("edit_girne_members", "Can edit girneAdmin members"),
                ],
                "verbose_name": "Üyeler",
                "verbose_name_plural": "Üyeler",
            },
        ),
        migrations.AddField(
            model_name="member",
            name="school",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="schools.schools",
            ),
        ),
    ]
