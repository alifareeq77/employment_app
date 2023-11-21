# Generated by Django 4.2.7 on 2023-11-21 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('form_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='appliers',
            field=models.ManyToManyField(to='users_app.appliers'),
        ),
        migrations.AddField(
            model_name='form',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
