# Generated by Django 4.1.7 on 2023-03-23 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tthapp', '0003_rename_comments_contactus_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='reguser',
            fields=[
                ('name', models.TextField(max_length=255)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('password', models.TextField(max_length=255)),
            ],
            options={
                'db_table': 'reguser',
            },
        ),
    ]