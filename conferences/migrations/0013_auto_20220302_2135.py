# Generated by Django 3.2 on 2022-03-03 00:35

from django.db import migrations, models
import django.utils.timezone
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("conferences", "0012_resource_resourcefile_resourceimage_resourcelink"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contactinformation",
            old_name="created",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="contactinformation",
            old_name="last_update",
            new_name="updated_at",
        ),
        migrations.RenameField(
            model_name="country",
            old_name="created",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="country",
            old_name="last_update",
            new_name="updated_at",
        ),
        migrations.RenameField(
            model_name="event",
            old_name="created",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="event",
            old_name="last_update",
            new_name="updated_at",
        ),
        migrations.RenameField(
            model_name="grant",
            old_name="created",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="grant",
            old_name="last_update",
            new_name="updated_at",
        ),
        migrations.RenameField(
            model_name="profile",
            old_name="created",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="profile",
            old_name="last_update",
            new_name="updated_at",
        ),
        migrations.RenameField(
            model_name="resource",
            old_name="update_at",
            new_name="updated_at",
        ),
        migrations.RenameField(
            model_name="room",
            old_name="created",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="room",
            old_name="last_update",
            new_name="updated_at",
        ),
        migrations.RenameField(
            model_name="speakerpertalk",
            old_name="created",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="speakerpertalk",
            old_name="last_update",
            new_name="updated_at",
        ),
        migrations.RenameField(
            model_name="sponsor",
            old_name="created",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="sponsor",
            old_name="last_update",
            new_name="updated_at",
        ),
        migrations.RenameField(
            model_name="sponsorlevel",
            old_name="created",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="sponsorlevel",
            old_name="last_update",
            new_name="updated_at",
        ),
        migrations.RenameField(
            model_name="staticpage",
            old_name="created",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="staticpage",
            old_name="last_update",
            new_name="updated_at",
        ),
        migrations.RenameField(
            model_name="talk",
            old_name="created",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="talk",
            old_name="last_update",
            new_name="updated_at",
        ),
        migrations.RenameField(
            model_name="talkroom",
            old_name="created",
            new_name="created_at",
        ),
        migrations.RenameField(
            model_name="talkroom",
            old_name="last_update",
            new_name="updated_at",
        ),
        migrations.RemoveField(
            model_name="resourceimage",
            name="file",
        ),
        migrations.AddField(
            model_name="resourceimage",
            name="photo",
            field=sorl.thumbnail.fields.ImageField(
                blank=True, default=None, null=True, upload_to="resources/"
            ),
        ),
        migrations.AddField(
            model_name="socialmedia",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="socialmedia",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="speaker",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="speaker",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="resourcefile",
            name="file",
            field=models.FileField(
                blank=True, default=None, null=True, upload_to="resources/"
            ),
        ),
        migrations.AlterField(
            model_name="speaker",
            name="photo",
            field=sorl.thumbnail.fields.ImageField(
                blank=True, default=None, null=True, upload_to="speakers/photos/"
            ),
        ),
        migrations.AlterField(
            model_name="sponsor",
            name="logo",
            field=sorl.thumbnail.fields.ImageField(
                blank=True, default=None, null=True, upload_to="sponsors/logos/"
            ),
        ),
    ]
