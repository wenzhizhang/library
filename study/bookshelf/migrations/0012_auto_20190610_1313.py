# Generated by Django 2.2.1 on 2019-06-10 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0011_auto_20190610_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='chinese_name',
            field=models.CharField(blank=True, default=None, max_length=200, verbose_name='中文译名'),
        ),
        migrations.AlterField(
            model_name='book',
            name='original_name',
            field=models.CharField(max_length=200, verbose_name='名称'),
        ),
    ]
