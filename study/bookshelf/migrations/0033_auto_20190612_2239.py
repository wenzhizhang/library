# Generated by Django 2.2.2 on 2019-06-12 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0032_auto_20190612_1701'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['nation']},
        ),
    ]
