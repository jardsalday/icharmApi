# Generated by Django 2.2.5 on 2020-01-26 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test2', '0015_auto_20200126_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientuserprofile',
            name='phone_number',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
