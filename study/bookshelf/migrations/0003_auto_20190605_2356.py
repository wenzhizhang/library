# Generated by Django 2.2.2 on 2019-06-05 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0002_book_bookshelf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='thumb_image',
            field=models.ImageField(upload_to='image/', verbose_name='Thumb'),
        ),
    ]