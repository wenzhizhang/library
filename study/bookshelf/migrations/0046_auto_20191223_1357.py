# Generated by Django 2.2.2 on 2019-12-23 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0045_auto_20191223_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]