# Generated by Django 2.2.1 on 2019-06-10 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0013_auto_20190610_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookshelf',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
