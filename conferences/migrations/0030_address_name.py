# Generated by Django 3.2 on 2022-05-31 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("conferences", "0029_auto_20220531_2031"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="name",
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
