# Generated by Django 3.2 on 2022-11-07 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0107_auto_20221105_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='nation',
            field=models.CharField(choices=[('未知', '未知'), ('中国', '中国'), ('德国', '德国'), ('英国', '英国'), ('法国', '法国'), ('美国', '美国'), ('俄罗斯', '俄罗斯'), ('日本', '日本'), ('加拿大', '加拿大'), ('前苏联', '前苏联'), ('爱尔兰', '爱尔兰'), ('澳大利亚', '澳大利亚'), ('以色列', '以色列'), ('瑞士', '瑞士'), ('阿根廷', '阿根廷'), ('哥伦比亚', '哥伦比亚'), ('奥地利', '奥地利'), ('西班牙', '西班牙'), ('挪威', '挪威'), ('瑞典', '瑞典'), ('意大利', '意大利'), ('希腊', '希腊'), ('比利时', '比利时'), ('墨西哥', '墨西哥'), ('荷兰', '荷兰'), ('巴西', '巴西'), ('波兰', '波兰'), ('伊朗', '伊朗'), ('古巴', '古巴'), ('波斯', '波斯'), ('智利', '智利'), ('南非', '南非'), ('马来西亚', '马来西亚'), ('捷克', '捷克')], max_length=100, verbose_name='国籍'),
        ),
    ]
