# Generated by Django 2.2.5 on 2019-12-30 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test2', '0010_auto_20191230_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicuserprofile',
            name='position',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
