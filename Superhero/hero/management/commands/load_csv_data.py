from django.core.management import BaseCommand
from pathlib import Path
from hero.models import Hero, Article
from csv import reader

class Command(BaseCommand):
    def handle(self, *args, **options):
        load_csv_data()

def load_csv_data():
    hero_path = Path("HeroData.csv")
    if hero_path.exists():
        with open(hero_path) as f:
            return [row for row in reader(f)]
            
    article_path = Path("ArticleData.csv")
    if article_path.exists():
        with open(article_path) as f:
            return [row for row in reader(f)]
