# Generated by Django 3.0.3 on 2020-03-24 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecohub', '0008_auto_20200317_0645'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.DateField(verbose_name='date published')),
                ('title', models.CharField(max_length=255)),
                ('abstract', models.TextField(default='Abstract')),
                ('content', models.TextField()),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='ecohub.NewsCategory', verbose_name='Category')),
            ],
        ),
    ]
