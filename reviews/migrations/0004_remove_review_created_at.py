# Generated by Django 4.1.5 on 2023-02-10 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0003_review_number_of_players"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="review",
            name="created_at",
        ),
    ]
