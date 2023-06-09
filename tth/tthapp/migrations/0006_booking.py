# Generated by Django 4.1.7 on 2023-04-01 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tthapp', '0005_user_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('firstname', models.TextField(max_length=255)),
                ('lastname', models.TextField(max_length=255)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('phno', models.IntegerField()),
                ('depdate', models.DateField(max_length=10)),
                ('arvdate', models.DateField(max_length=10)),
                ('guest', models.TextField(max_length=6)),
                ('room', models.TextField(max_length=15)),
            ],
            options={
                'db_table': 'booking',
            },
        ),
    ]
