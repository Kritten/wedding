# Generated by Django 2.2.6 on 2019-11-26 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='food',
            field=models.TextField(blank=True, null=True),
        ),
    ]
