# Generated by Django 2.1.3 on 2018-11-24 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solos', '0005_auto_20181120_2055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='solo',
            options={'ordering': ['track', 'start_time']},
        ),
        migrations.RemoveField(
            model_name='solo',
            name='album',
        ),
    ]
