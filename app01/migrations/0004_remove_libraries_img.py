# Generated by Django 4.1.3 on 2023-03-16 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_libraries_wx_bookid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libraries',
            name='img',
        ),
    ]
