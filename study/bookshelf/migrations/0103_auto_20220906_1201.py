# Generated by Django 3.1.6 on 2022-09-06 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0102_auto_20220906_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='registered',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=20, verbose_name='登记状态'),
        ),
    ]
