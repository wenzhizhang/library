# Generated by Django 2.2.1 on 2019-06-10 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0008_auto_20190610_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='chinese_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='中文名'),
        ),
        migrations.AlterField(
            model_name='author',
            name='dynasty',
            field=models.CharField(blank=True, choices=[('XIA', '夏'), ('SHANG', '商'), ('WESTZHOU', '西周'), ('EASTZHOU', '东周'), ('CHUNQIU', '春秋'), ('ZHANGUO', '战国'), ('QIN', '秦'), ('WESTHAN', '西汉'), ('EASTHAN', '东汉'), ('WEI', '魏'), ('SHU', '蜀'), ('WU', '吴'), ('WESTJIN', '西晋'), ('EASTJIN', '东晋'), ('NANBEICHAO', '南北朝'), ('SUI', '隋'), ('TANG', '唐'), ('WUDAI', '五代十国'), ('NORTHSONG', '北宋'), ('SOUTHSONG', '南宋'), ('YUAN', '元'), ('MING', '明'), ('QING', '清'), ('MINGUO', '民国'), ('DANGDAI', '当代')], max_length=100, verbose_name='朝代'),
        ),
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=200, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='author',
            name='nation',
            field=models.CharField(choices=[('CHINA', '中国'), ('BRITAIN', '英国'), ('FRANCE', '法国'), ('AMERICA', '美国'), ('RUSSIA', '俄国'), ('JAPAN', '日本'), ('IRELAND', '爱尔兰'), ('AUSTRALIA', '澳大利亚'), ('ISRAEL', '以色列')], max_length=100, verbose_name='国籍'),
        ),
    ]
