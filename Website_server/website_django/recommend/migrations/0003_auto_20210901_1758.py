# Generated by Django 3.2.6 on 2021-09-01 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0002_auto_20210901_1726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='movie_id',
            new_name='movieId',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='user_id',
            new_name='userId',
        ),
    ]
