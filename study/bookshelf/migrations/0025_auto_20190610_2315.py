# Generated by Django 2.2.2 on 2019-06-10 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0024_auto_20190610_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='dynasty',
            field=models.CharField(blank=True, choices=[('夏', '夏'), ('商', '商'), ('西周', '西周'), ('东周', '东周'), ('春秋', '春秋'), ('战国', '战国'), ('秦', '秦'), ('西汉', '西汉'), ('东汉', '东汉'), ('魏', '魏'), ('蜀', '蜀'), ('吴', '吴'), ('西晋', '西晋'), ('东晋', '东晋'), ('南北朝', '南北朝'), ('隋', '隋'), ('唐', '唐'), ('五代', '五代'), ('北宋', '北宋'), ('南宁', '南宋'), ('元', '元'), ('明', '明'), ('清', '清'), ('民国', '民国'), ('当代', '当代')], max_length=100),
        ),
        migrations.AlterField(
            model_name='author',
            name='nation',
            field=models.CharField(choices=[('中国', '中国'), ('英国', '英国'), ('法国', '法国'), ('美国', '美国'), ('俄国', '俄国'), ('日本', '日本'), ('爱尔兰', '爱尔兰'), ('澳大利亚', '澳大利亚'), ('以色列', '以色列')], max_length=100),
        ),
    ]
