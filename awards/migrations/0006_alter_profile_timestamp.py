# Generated by Django 3.2.5 on 2021-07-19 20:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0005_alter_profile_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 19, 20, 33, 11, 356457, tzinfo=utc)),
        ),
    ]