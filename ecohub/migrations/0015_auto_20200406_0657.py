# Generated by Django 3.0.3 on 2020-04-06 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecohub', '0014_auto_20200406_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='current_funds',
            field=models.BigIntegerField(default=0),
        ),
    ]