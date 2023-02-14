# Generated by Django 4.1.5 on 2023-02-10 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="TennisCourt",
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
                ("name", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=50)),
                (
                    "district",
                    models.CharField(
                        choices=[
                            ("OL", "Olmazor"),
                            ("BE", "Bektemir"),
                            ("YU", "Yunusobod"),
                            ("MU", "Mirzo Ulug'bek"),
                            ("SH", "Shayxontohur"),
                            ("UC", "Uchtepa"),
                            ("CH", "Chilonzor"),
                            ("MI", "Mirobod"),
                            ("SE", "Sergeli"),
                            ("YS", "Yakkasaroy"),
                            ("YA", "Yashnobod"),
                            ("TV", "Toshkent Viloyati"),
                            ("ZA", "Zangiota"),
                            ("QB", "Qibray"),
                            ("BO", "Bo'stonliq"),
                        ],
                        max_length=2,
                    ),
                ),
                ("phone", models.CharField(max_length=50)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("website", models.URLField(blank=True, null=True)),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
                ("opens_at", models.TimeField(null=True)),
                ("closes_at", models.TimeField(null=True)),
                ("lights", models.BooleanField(default=True)),
                ("indoor", models.BooleanField(default=False)),
                ("public", models.BooleanField(default=True)),
                (
                    "surface",
                    models.CharField(
                        choices=[("H", "Hard"), ("C", "Clay"), ("G", "Grass")],
                        max_length=1,
                    ),
                ),
                ("court_count", models.IntegerField(default=1)),
                (
                    "user",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]