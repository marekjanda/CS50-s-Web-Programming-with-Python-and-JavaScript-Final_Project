# Generated by Django 3.0.3 on 2020-04-06 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecohub', '0011_auto_20200401_0553'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('published', models.DateField(auto_now_add=True)),
                ('abstract', models.TextField()),
                ('description', models.TextField()),
                ('target_funds', models.BigIntegerField()),
                ('current_funds', models.BigIntegerField()),
                ('attachement', models.FileField(upload_to='')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='ecohub.NewsCategory', verbose_name='Category')),
            ],
        ),
    ]
