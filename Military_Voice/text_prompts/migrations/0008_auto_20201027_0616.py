# Generated by Django 2.1.2 on 2020-10-27 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text_prompts', '0007_auto_20201020_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sentence',
            name='recorded',
        ),
        migrations.AddField(
            model_name='sentence',
            name='count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
