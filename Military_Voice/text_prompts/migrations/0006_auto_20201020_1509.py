# Generated by Django 2.1.2 on 2020-10-20 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('text_prompts', '0005_sentence_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sentence',
            old_name='id',
            new_name='uid',
        ),
    ]
