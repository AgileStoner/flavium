# Generated by Django 4.1.5 on 2023-02-04 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('bookings', '0008_alter_booking_content_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]
