# Generated by Django 2.2.5 on 2020-02-23 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRU', '0025_auto_20200223_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='created_at',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
