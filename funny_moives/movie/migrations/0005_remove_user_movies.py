# Generated by Django 4.0.4 on 2022-08-16 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_movieview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='movies',
        ),
    ]