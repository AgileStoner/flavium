# Generated by Django 4.1.5 on 2023-02-10 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0002_remove_review_content_type_remove_review_object_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="number_of_players",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
