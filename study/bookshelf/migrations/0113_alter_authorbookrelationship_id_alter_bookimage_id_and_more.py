# Generated by Django 4.1.3 on 2022-11-09 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0112_alter_author_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorbookrelationship',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bookimage',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='taggeditem',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
