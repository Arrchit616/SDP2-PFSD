# Generated by Django 4.1.7 on 2023-04-01 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tthapp', '0008_hotel_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='firstname',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='booking',
            name='lastname',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='booking',
            name='room',
            field=models.CharField(max_length=15),
        ),
    ]
