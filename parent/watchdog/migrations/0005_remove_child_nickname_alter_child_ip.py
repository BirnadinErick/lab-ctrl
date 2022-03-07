# Generated by Django 4.0.2 on 2022-03-07 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchdog', '0004_rename_nick_name_child_nickname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='nickname',
        ),
        migrations.AlterField(
            model_name='child',
            name='ip',
            field=models.CharField(max_length=15, unique=True, verbose_name='IP-Addr of the child'),
        ),
    ]