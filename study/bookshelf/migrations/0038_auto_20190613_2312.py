# Generated by Django 2.2.2 on 2019-06-13 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0037_auto_20190613_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='第一作者'),
        ),
    ]
