# Generated by Django 2.2.1 on 2019-06-10 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0021_auto_20190610_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='binding_type',
            field=models.CharField(choices=[('精装', '精装'), ('平装', '平装'), ('线装', '线装'), ('线装', '线装')], max_length=20, verbose_name='装帧'),
        ),
    ]
