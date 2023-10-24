# Generated by Django 4.2.6 on 2023-10-23 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("members", "0002_delete_memberaddress_delete_members"),
    ]

    operations = [
        migrations.CreateModel(
            name="Campus",
            fields=[
                ("CampusID", models.AutoField(primary_key=True, serialize=False)),
                ("FranchiseState", models.BooleanField()),
                ("Phone", models.CharField(max_length=255)),
                ("Email", models.EmailField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="CampusAddress",
            fields=[
                (
                    "CampusAddressID",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("FullAddress", models.CharField(max_length=255)),
                ("District", models.CharField(max_length=50)),
                ("City", models.CharField(max_length=50)),
                ("PostalCode", models.IntegerField()),
                ("AuthorizedFirstName", models.CharField(max_length=50)),
                ("AuthorizedLastName", models.CharField(max_length=50)),
                ("AuthorizedEmail", models.EmailField(max_length=100)),
                ("AuthorizedPhone", models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name="Class",
            fields=[
                ("ClassID", models.AutoField(primary_key=True, serialize=False)),
                ("ClassName", models.CharField(max_length=255)),
                ("ClassDescription", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="StudentLevels",
            fields=[
                ("LevelID", models.AutoField(primary_key=True, serialize=False)),
                ("LevelName", models.CharField(max_length=100)),
                (
                    "CampusID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="members.campus"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Members",
            fields=[
                ("MemberID", models.AutoField(primary_key=True, serialize=False)),
                ("UserType", models.CharField(max_length=100)),
                ("Identification", models.CharField(max_length=255, unique=True)),
                ("PhoneNumber", models.CharField(max_length=20)),
                ("FirstName", models.CharField(max_length=255)),
                ("LastName", models.CharField(max_length=255)),
                ("BirthDate", models.DateField()),
                ("Email", models.EmailField(max_length=255, unique=True)),
                ("PasswordHash", models.CharField(max_length=255)),
                ("Gender", models.CharField(max_length=100)),
                ("RegistrationState", models.CharField(max_length=100)),
                ("RegistrationDate", models.DateTimeField()),
                ("LastLogin", models.DateField()),
                ("LastUpdated", models.DateTimeField()),
                ("IsActive", models.BooleanField()),
                ("IPAddress", models.CharField(max_length=45)),
                ("Season", models.DateField()),
                (
                    "CampusID",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="members.campus",
                    ),
                ),
                (
                    "ClassID",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="members.class",
                    ),
                ),
                (
                    "LevelID",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="members.studentlevels",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="campus",
            name="CampusAddressID",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="members.campusaddress"
            ),
        ),
    ]