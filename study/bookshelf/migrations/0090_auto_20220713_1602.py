# Generated by Django 3.1.6 on 2022-07-13 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0089_auto_20220713_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(blank=True, max_length=30, verbose_name='分类'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.DateField(blank=True, verbose_name='出版日期'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='publisher', to='bookshelf.publisher', verbose_name='出版社'),
        ),
        migrations.AlterField(
            model_name='book',
            name='thumb_image',
            field=models.ImageField(blank=True, default=None, upload_to='image/books/', verbose_name='缩略图'),
        ),
    ]
