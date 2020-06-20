# Generated by Django 2.2.5 on 2019-11-20 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRU', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('systolic', models.CharField(max_length=100)),
                ('diastolic', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('cholesterol', models.CharField(max_length=100)),
            ],
        ),
    ]