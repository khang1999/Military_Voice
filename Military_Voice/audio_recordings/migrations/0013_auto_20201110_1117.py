# Generated by Django 2.1.2 on 2020-11-10 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio_recordings', '0012_auto_20201110_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recording',
            name='verified',
            field=models.IntegerField(default=0),
        ),
    ]
