# Generated by Django 4.2.11 on 2024-04-15 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_userprofile_midlle_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='midlle_name',
            new_name='middle_name',
        ),
    ]
