# Generated by Django 3.1.4 on 2020-12-30 09:54

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('bookshelf', '0081_book_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
