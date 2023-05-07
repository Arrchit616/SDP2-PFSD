# Generated by Django 4.1.7 on 2023-04-02 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tthapp', '0009_alter_booking_firstname_alter_booking_lastname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardno', models.TextField(max_length=255)),
                ('expdate', models.TextField(max_length=255)),
                ('cvv', models.TextField(max_length=255)),
                ('cardholder', models.TextField(max_length=255)),
            ],
            options={
                'db_table': 'payment',
            },
        ),
    ]