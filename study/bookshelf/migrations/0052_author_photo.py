# Generated by Django 2.2.2 on 2020-02-07 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0051_auto_20200207_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='image/authors/', verbose_name='相片'),
        ),
    ]