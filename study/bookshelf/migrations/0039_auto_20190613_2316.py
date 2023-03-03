# Generated by Django 2.2.2 on 2019-06-13 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0038_auto_20190613_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='bookshelf.Author', verbose_name='第一作者'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author_2nd',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_2nd', to='bookshelf.Author', verbose_name='第二作者'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author_3rd',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_3rd', to='bookshelf.Author', verbose_name='第三作者'),
        ),
    ]
