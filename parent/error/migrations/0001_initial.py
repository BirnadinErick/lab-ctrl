# Generated by Django 4.0.2 on 2022-02-15 10:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Error',
            fields=[
                ('eid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Unique ID for error')),
                ('title', models.CharField(max_length=100, verbose_name='Title of the error')),
                ('isHandled', models.BooleanField(verbose_name='Isthe error Handled or not?')),
                ('timestamp', models.FloatField(verbose_name='Timestamp of the time the error was recorded')),
                ('victim', models.CharField(blank=True, max_length=36, verbose_name='ID of the victim')),
                ('ecode', models.IntegerField(verbose_name='Error Code')),
            ],
            options={
                'verbose_name': 'Error',
                'verbose_name_plural': 'Errors',
            },
        ),
    ]
