# Generated by Django 2.1.2 on 2020-08-19 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('text_prompts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sentences',
            new_name='Sentence',
        ),
    ]
