# Generated by Django 2.1.2 on 2020-11-09 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audio_recordings', '0009_recording_verfied'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recording',
            old_name='verfied',
            new_name='verified',
        ),
    ]
