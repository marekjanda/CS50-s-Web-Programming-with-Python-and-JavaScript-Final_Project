# Generated by Django 3.0.3 on 2020-04-15 05:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecohub', '0027_auto_20200415_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sent',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 15, 6, 23, 39, 238269), verbose_name='date sent'),
        ),
        migrations.AlterField(
            model_name='project',
            name='attachment',
            field=models.FileField(blank=True, upload_to='uploads/%Y/%m/%d/'),
        ),
    ]