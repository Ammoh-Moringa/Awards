# Generated by Django 3.2.5 on 2021-07-17 08:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0002_auto_20210717_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 17, 8, 39, 20, 573224, tzinfo=utc)),
        ),
    ]
