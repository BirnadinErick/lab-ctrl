# Generated by Django 4.0.2 on 2022-02-15 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchdog', '0002_child_stask_child'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='nurse_check_type',
            field=models.IntegerField(verbose_name='Nurse Check Type'),
        ),
    ]