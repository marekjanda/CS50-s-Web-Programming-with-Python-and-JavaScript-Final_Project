# Generated by Django 3.0.3 on 2020-03-13 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_category', models.CharField(max_length=255)),
                ('category_summary', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'News Categories',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=511)),
            ],
        ),
    ]
