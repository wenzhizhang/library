# Generated by Django 2.2.2 on 2019-06-06 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0003_auto_20190605_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='link',
            field=models.CharField(max_length=200, null=True),
        ),
    ]