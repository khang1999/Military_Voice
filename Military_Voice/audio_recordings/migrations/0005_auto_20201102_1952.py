# Generated by Django 2.1.2 on 2020-11-02 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio_recordings', '0004_auto_20201102_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordings',
            name='audiofile',
            field=models.CharField(max_length=1000),
        ),
    ]