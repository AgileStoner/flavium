# Generated by Django 4.1.5 on 2023-01-30 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='registration_date',
        ),
    ]
