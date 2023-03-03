# Generated by Django 2.2.2 on 2019-12-23 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0046_auto_20191223_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='introduction',
            field=models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='简介'),
        ),
        migrations.AddField(
            model_name='book',
            name='read_state',
            field=models.CharField(choices=[('未读', '未读'), ('在读', '在读'), ('已读', '已读')], default='未读', max_length=20, verbose_name='阅读状态'),
        ),
    ]
