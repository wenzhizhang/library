# Generated by Django 4.1.3 on 2022-11-12 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0113_alter_authorbookrelationship_id_alter_bookimage_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(blank=True, max_length=100, verbose_name='分类'),
        ),
    ]