# Generated by Django 2.2.5 on 2019-12-30 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test2', '0004_auto_20191230_0938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]