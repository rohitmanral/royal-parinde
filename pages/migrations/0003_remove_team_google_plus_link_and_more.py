# Generated by Django 4.0.6 on 2022-10-02 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20220710_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='google_plus_link',
        ),
        migrations.RemoveField(
            model_name='team',
            name='twitter_link',
        ),
    ]