# Generated by Django 3.2 on 2022-04-19 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0017_event_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='asked_for_a_grant',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_organizer',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_speaker',
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
