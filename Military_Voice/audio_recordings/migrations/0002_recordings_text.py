# Generated by Django 2.1.2 on 2020-10-28 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio_recordings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recordings',
            name='text',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
