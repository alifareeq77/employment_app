# Generated by Django 4.2.7 on 2023-11-25 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0006_remove_customuser_first_name_and_more'),
        ('form_app', '0004_formappliers'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(choices=[(5, 'THREE MONTHS'), (9, 'SIX MONTHS')])),
                ('transaction_id', models.CharField(max_length=256)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users_app.appliers')),
            ],
        ),
    ]