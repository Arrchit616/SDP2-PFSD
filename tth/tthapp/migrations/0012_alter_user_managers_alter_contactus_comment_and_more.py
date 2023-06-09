# Generated by Django 4.1.7 on 2023-05-05 18:53

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tthapp', '0011_alter_payment_expdate'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='contactus',
            name='comment',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='firstname',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='lastname',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forget_password_token', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tthapp.user')),
            ],
        ),
    ]
