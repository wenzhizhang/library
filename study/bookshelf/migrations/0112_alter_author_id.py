# Generated by Django 4.1.3 on 2022-11-09 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0111_book_compose_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]