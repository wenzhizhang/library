# Generated by Django 2.2.2 on 2020-02-10 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0056_auto_20200210_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='introduction',
            field=models.TextField(blank=True, default=None, max_length=1500, null=True, verbose_name='简介'),
        ),
    ]