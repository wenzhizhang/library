# Generated by Django 2.2.2 on 2020-02-07 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0048_auto_20191223_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='intro',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
