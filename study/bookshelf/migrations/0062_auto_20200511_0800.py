# Generated by Django 2.2.3 on 2020-05-11 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0061_auto_20200510_2314'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['name']},
        ),
    ]
