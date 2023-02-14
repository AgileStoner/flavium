# Generated by Django 4.1.5 on 2023-02-11 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("bookings", "0012_alter_booking_status"),
        ("reviews", "0005_review_content_type_review_object_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="booking",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="bookings.booking"
            ),
        ),
    ]
