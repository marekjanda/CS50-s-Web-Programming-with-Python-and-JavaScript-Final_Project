# Generated by Django 3.0.3 on 2020-03-13 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecohub', '0002_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='news_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='ecohub.NewsCategory', verbose_name='Category'),
        ),
    ]
