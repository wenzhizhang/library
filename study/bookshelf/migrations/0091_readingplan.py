# Generated by Django 3.2 on 2022-07-20 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0090_auto_20220713_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadingPlan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='计划名')),
                ('description', models.TextField(verbose_name='计划详情')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('books', models.ManyToManyField(to='bookshelf.Book')),
            ],
        ),
    ]