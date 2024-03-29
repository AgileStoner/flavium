# Generated by Django 4.1.6 on 2023-03-11 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="images",
            name="content_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AlterField(
            model_name="images",
            name="object_id",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
