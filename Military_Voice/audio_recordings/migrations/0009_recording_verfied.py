# Generated by Django 2.1.2 on 2020-11-09 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio_recordings', '0008_auto_20201106_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='recording',
            name='verfied',
            field=models.BooleanField(default=False),
        ),
    ]