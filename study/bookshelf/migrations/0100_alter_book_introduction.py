# Generated by Django 3.2 on 2022-09-01 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0099_alter_author_nation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='introduction',
            field=models.TextField(blank=True, default=None, max_length=2000, null=True, verbose_name='简介'),
        ),
    ]
