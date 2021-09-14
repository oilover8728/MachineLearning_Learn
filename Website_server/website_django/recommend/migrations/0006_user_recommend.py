# Generated by Django 3.2.6 on 2021-09-06 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0005_rename_index_movie_index_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_recommend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField(default=0)),
                ('top1_movie', models.IntegerField(default=0)),
                ('top2_movie', models.IntegerField(default=0)),
            ],
        ),
    ]