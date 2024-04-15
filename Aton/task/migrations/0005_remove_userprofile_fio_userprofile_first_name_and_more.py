# Generated by Django 4.2.11 on 2024-04-15 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_userprofile_fio_alter_client_acc_num_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='fio',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(default='Иванов', max_length=128),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(default='Иван', max_length=128),
        ),
    ]