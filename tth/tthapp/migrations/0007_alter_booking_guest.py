# Generated by Django 4.1.7 on 2023-04-01 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tthapp', '0006_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='guest',
            field=models.IntegerField(),
        ),
    ]