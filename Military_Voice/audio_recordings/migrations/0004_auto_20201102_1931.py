# Generated by Django 2.1.2 on 2020-11-02 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio_recordings', '0003_auto_20201102_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recordings',
            name='duration',
        ),
        migrations.AlterField(
            model_name='recordings',
            name='audiofile',
            field=models.CharField(max_length=100),
        ),
    ]
