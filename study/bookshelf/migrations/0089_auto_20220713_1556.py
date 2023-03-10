# Generated by Django 3.1.6 on 2022-07-13 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0088_auto_20220713_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.IntegerField(default=1, verbose_name='页数'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.FloatField(blank=True, verbose_name='定价'),
        ),
        migrations.AlterField(
            model_name='book',
            name='purchase_date',
            field=models.DateField(blank=True, verbose_name='购入日期'),
        ),
        migrations.AlterField(
            model_name='book',
            name='purchase_price',
            field=models.FloatField(blank=True, verbose_name='购入价格'),
        ),
    ]
