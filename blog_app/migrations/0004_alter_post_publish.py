# Generated by Django 3.2.5 on 2021-08-09 14:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_auto_20210808_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 9, 14, 27, 5, 250972, tzinfo=utc)),
        ),
    ]
