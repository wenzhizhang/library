# Generated by Django 2.2.2 on 2019-12-12 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0043_auto_20190623_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='id',
            field=models.IntegerField(default=1),
        ),
    ]
