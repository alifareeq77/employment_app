# Generated by Django 4.2.7 on 2023-11-25 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0005_remove_appliers_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='last_name',
        ),
    ]