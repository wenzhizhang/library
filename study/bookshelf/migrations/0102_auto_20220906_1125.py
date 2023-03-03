# Generated by Django 3.1.6 on 2022-09-06 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0101_auto_20220903_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='edition',
            field=models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='版次'),
        ),
        migrations.AddField(
            model_name='book',
            name='print',
            field=models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='印次'),
        ),
        migrations.AddField(
            model_name='book',
            name='printed_number',
            field=models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='印数'),
        ),
    ]
