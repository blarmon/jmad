# Generated by Django 2.1.3 on 2018-11-21 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solos', '0003_auto_20181118_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='solo',
            name='slug',
            field=models.SlugField(default='n/a'),
            preserve_default=False,
        ),
    ]
