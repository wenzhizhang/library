# Generated by Django 2.2.2 on 2019-06-13 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0036_auto_20190613_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='nation',
            field=models.CharField(choices=[('中', '中'), ('德', '德'), ('英', '英'), ('法', '法'), ('美', '美'), ('俄', '俄'), ('日', '日'), ('加', '加'), ('爱尔兰', '爱尔兰'), ('澳', '澳'), ('以色列', '以色列'), ('瑞士', '瑞士'), ('阿根廷', '阿根廷')], max_length=100),
        ),
    ]
