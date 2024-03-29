# Generated by Django 4.1.5 on 2023-02-10 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("reviews", "0004_remove_review_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="content_type",
            field=models.ForeignKey(
                limit_choices_to={"model__in": ("venues", "tenniscourt")},
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AddField(
            model_name="review",
            name="object_id",
            field=models.PositiveIntegerField(null=True),
        ),
    ]
