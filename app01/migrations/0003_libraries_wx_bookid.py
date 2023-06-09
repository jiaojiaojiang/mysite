# Generated by Django 4.1.3 on 2023-03-11 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_rename_jiaoyu_jy_rename_wenxue_wx_rename_zhexue_zx'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libraries',
            fields=[
                ('bookid', models.AutoField(primary_key=True, serialize=False)),
                ('bookname', models.CharField(blank=True, max_length=255, null=True)),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('des', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('img', models.TextField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'libraries',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='wx',
            name='bookid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
