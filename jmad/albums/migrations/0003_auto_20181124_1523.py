# Generated by Django 2.1.3 on 2018-11-24 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_track_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='track',
            options={'ordering': ['album', 'track_number']},
        ),
    ]
