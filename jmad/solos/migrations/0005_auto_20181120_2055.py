# Generated by Django 2.1.3 on 2018-11-21 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('solos', '0004_solo_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solo',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albums.Track'),
        ),
    ]
