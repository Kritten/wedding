# Generated by Django 2.2.6 on 2019-10-28 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_event_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100, unique=True)),
                ('link', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('count_players_min', models.IntegerField(default=2)),
                ('count_players_max', models.IntegerField(default=2)),
                ('minutes_playtime_min', models.IntegerField()),
                ('minutes_playtime_max', models.IntegerField()),
                ('is_coop', models.BooleanField()),
                ('minutes_explanation', models.IntegerField()),
                ('genres', models.ManyToManyField(related_name='games', to='api.Genre')),
                ('images', models.ManyToManyField(related_name='games', to='api.Image')),
                ('moods', models.ManyToManyField(related_name='games', to='api.Mood')),
                ('types', models.ManyToManyField(related_name='games', to='api.Type')),
            ],
        ),
    ]
