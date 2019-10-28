import csv

from django.core.management import BaseCommand

from api.models import Game, Genre, Mood, Type


class Command(BaseCommand):
    help = 'Import games'

    def handle(self, *args, **options):
        with open('games.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(row)
                game = Game.objects.create(
                    title=row['title'],
                    description=row['description'],
                    count_players_min=row['count_players_min'],
                    count_players_max=row['count_players_max'],
                    minutes_playtime_min=row['minutes_playtime_min'],
                    minutes_playtime_max=row['minutes_playtime_max'],
                    is_coop=True if row['is_coop'] == 'TRUE' else False,
                    minutes_explanation=row['minutes_explanation'],
                )

                for genre in row['genres'].split(','):
                    game.genres.add(
                        Genre.objects.get_or_create(
                            label=genre.strip()
                        )[0]
                    )

                for mood in row['moods'].split(','):
                    game.moods.add(
                        Mood.objects.get_or_create(
                            label=mood.strip()
                        )[0]
                    )

                for type in row['types'].split(','):
                    game.types.add(
                        Type.objects.get_or_create(
                            label=type.strip()
                        )[0]
                    )

                game.save()
