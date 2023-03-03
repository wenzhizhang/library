# Generated by Django 3.2 on 2022-07-22 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0091_readingplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorBookRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='bookshelf.author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='bookshelf.book')),
            ],
        ),
    ]
