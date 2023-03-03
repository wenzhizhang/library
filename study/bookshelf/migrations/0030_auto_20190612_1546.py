# Generated by Django 2.2.1 on 2019-06-12 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0029_auto_20190612_0604'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_2nd',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='第二作者'),
        ),
        migrations.AddField(
            model_name='book',
            name='author_3rd',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='第三作者'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, default=None, max_length=100, verbose_name='第一作者'),
        ),
    ]
