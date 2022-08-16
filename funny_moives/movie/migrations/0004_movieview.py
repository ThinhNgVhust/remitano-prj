# Generated by Django 4.0.4 on 2022-08-16 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_alter_movie_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('creator_mail', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
    ]