# Generated by Django 2.2.3 on 2020-05-13 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0067_booklist'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Booklist',
            new_name='BookCollection',
        ),
    ]
