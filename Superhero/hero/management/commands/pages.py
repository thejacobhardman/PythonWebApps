from django.core.management.base import BaseCommand
from requests import get

class Command(BaseCommand):
    def handle(self, *args, **optionals):
        response = get("https://shrinking-world.com")
        print("Shrinking Word has: " + str(len(response.text)) + " characters.")
