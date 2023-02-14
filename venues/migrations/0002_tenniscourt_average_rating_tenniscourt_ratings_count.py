# Generated by Django 4.1.6 on 2023-02-12 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("venues", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tenniscourt",
            name="average_rating",
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name="tenniscourt",
            name="ratings_count",
            field=models.IntegerField(default=0),
        ),
    ]
