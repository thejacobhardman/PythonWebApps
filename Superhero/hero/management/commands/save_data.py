from django.core.management import BaseCommand
from hero.models import Hero, Article
from json import dump
from csv import writer

class Command(BaseCommand):
    def handle(self, *args, **options):
        save_data()

def save_data():
    hero_data = [hero for hero in Hero.objects.all().values()]
    article_data = [article for article in Article.objects.all().values()]

    with open("HeroData.json", "w") as f:
        dump(hero_data, f, indent=4)

    with open("HeroData.csv", "w", newline='') as f:
        writer(f).writerows(hero_data)

    with open("ArticleData.json", "w") as f:
        dump(article_data, f, indent=4)

    with open("ArticleData.csv", "w", newline='') as f:
        writer(f).writerows(article_data)
