# Generated by Django 3.2 on 2022-05-21 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("conferences", "0020_alter_eventregistration_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="sponsor",
            name="url",
            field=models.CharField(
                blank=True, default="https://", max_length=200, null=True
            ),
        ),
    ]
