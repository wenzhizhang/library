# Generated by Django 4.1.3 on 2022-11-08 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('taggit', '0006_mytag'),
        ('bookshelf', '0109_alter_author_nation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(choices=[('中文', '中文'), ('繁体中文', '繁体中文'), ('英文', '英文'), ('中文/英文', '中文/英文'), ('日文', '日文')], default='中文', max_length=30, verbose_name='正文语种'),
        ),
        migrations.AlterField(
            model_name='taggeditem',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_tagged_items', to='contenttypes.contenttype', verbose_name='content type'),
        ),
        migrations.AlterField(
            model_name='taggeditem',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_items', to='taggit.mytag'),
        ),
    ]
