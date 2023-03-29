# Generated by Django 4.1.6 on 2023-03-29 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("accounts", "0009_user_content_type_user_object_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="content_type",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"model__in": ("venues", "tenniscourt")},
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="contenttypes.contenttype",
            ),
        ),
    ]
