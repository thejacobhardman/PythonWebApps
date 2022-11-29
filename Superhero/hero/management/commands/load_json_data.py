from django.core.management import BaseCommand
from pathlib import Path
from hero.models import Hero, Article
from json import loads

class Command(BaseCommand):
    def handle(self, *args, **options):
        load_json_data()

def load_json_data():
    hero_path = Path("HeroData.json")
    if hero_path.exists():
        Hero.objects.all().delete()
        objects = loads(hero_path.read_text())

        for o in objects:
            Hero.objects.get_or_create(**o)

        for hero in Hero.objects.all().values():
            print(hero)

    article_path = Path("ArticleData.json")
    if article_path.exists():
        Article.objects.all().delete()
        objects = loads(article_path.read_text())

        for o in objects:
            Article.objects.get_or_create(**o)

        for article in Article.objects.all().values():
            print(hero)
