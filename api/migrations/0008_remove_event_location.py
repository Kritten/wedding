# Generated by Django 2.2.6 on 2019-10-26 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20191026_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='location',
        ),
    ]
