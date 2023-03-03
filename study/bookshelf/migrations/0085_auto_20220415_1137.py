# Generated by Django 2.2.3 on 2022-04-15 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0084_auto_20220413_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='dynasty',
            field=models.CharField(blank=True, choices=[('上古', '上古'), ('夏', '夏'), ('商', '商'), ('西周', '西周'), ('东周', '东周'), ('春秋', '春秋'), ('战国', '战国'), ('秦', '秦'), ('西汉', '西汉'), ('东汉', '东汉'), ('魏', '魏'), ('蜀', '蜀'), ('吴', '吴'), ('西晋', '西晋'), ('东晋', '东晋'), ('南北朝', '南北朝'), ('隋', '隋'), ('唐', '唐'), ('五代', '五代'), ('北宋', '北宋'), ('南宋', '南宋'), ('元', '元'), ('明', '明'), ('清', '清'), ('民国', '民国'), ('现代', '现代'), ('当代', '当代')], max_length=100, verbose_name='朝代'),
        ),
    ]