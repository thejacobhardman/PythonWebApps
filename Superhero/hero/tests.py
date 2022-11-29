from pathlib import Path
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from .models import Hero, Article
from page import get_web_page

from json import dump, loads
from csv import writer, reader

def create_test_heroes():
    print("Creating test heroes.")

def create_test_articles():
    print("Creating test articles.")

def export_hero_data_to_json():
    hero_data = [hero for hero in Hero.objects.all().values()]
    with open("HeroData.json", "w") as f:
        dump(hero_data, f, indent=4)

def export_article_data_to_json():
    article_data = [hero for hero in Article.objects.all().values()]
    with open("ArticleData.json", "w") as f:
        dump(article_data, f, indent=4)

def load_hero_data_from_json():
    path = Path("HeroData.json")
    if path.exists():
        objects = loads(path.read_text())
    for o in objects:
        Hero.objects.get_or_create(**o)

def load_article_data_from_json():
    path = Path("ArticleData.json")
    if path.exists():
        objects = loads(path.read_text())
    for o in objects:
        Article.objects.get_or_create(**o)

def export_hero_data_to_csv():
    hero_data = [hero for hero in Hero.objects.all().values()]
    with open("HeroData.csv", "w", newline='') as f:
        writer(f).writerows(hero_data)

def export_article_data_to_csv():
    article_data = [hero for hero in Article.objects.all().values()]
    with open("ArticleData.csv", "w", newline='') as f:
        writer(f).writerows(article_data)

def load_hero_data_from_csv():
    path = Path("HeroData.csv")
    if path.exists():
        with open(path) as f:
            return [row for row in reader(f)]

def load_article_data_from_csv():
    path = Path("ArticleData.csv")
    if path.exists():
        with open(path) as f:
            return [row for row in reader(f)]

# def user_args():
#     return dict(username="TESTER", email="test@test.us", password="secret")

# def test_user():
#     return get_user_model().objects.create_user(**user_args())

# class BlogAppTest(SimpleTestCase):
#     def check_page_text(self, url, min_chars, max_chars):
#         text = get_web_page(url)
#         num_chars = len(text)
#         self.assertGreaterEqual(num_chars, min_chars)
#         self.assertLessEqual(num_chars, max_chars)

#     def test_django(self):
#         self.assertTrue(True)

#     def test_pages(self):
#         self.check_page_text("https://google.com", 14000, 16000)
#         self.check_page_text("https://unco.edu", 31000, 42000)

# class BlogDataTest(TestCase):
#     def test_data_model(self):

#         # Add two articles
#         self.assertEqual(len(Article.objects.all()), 0)
#         Article.objects.create(title="Title 1", body="Body")
#         Article.objects.create(title="Title 2", body="Body")
#         self.assertEqual(len(Article.objects.all()), 2)

#         # Check the details
#         a = Article.objects.get(pk=2)
#         self.assertEqual(a.title, "Title 2")

#         # Edit the record
#         a.title = "New Title"
#         a.save()
#         self.assertEqual(a.title, "New Title")

#         # Delete a record
#         a.delete()
#         self.assertEqual(len(Article.objects.all()), 1)

# class ArticleViewsTest(TestCase):
#     def login(self):
#         response = self.client.login(
#             username=self.user.username, password=user_args()["password"]
#         )
#         self.assertEqual(response, True)

#     def setUp(self):
#         self.user = test_user()
#         self.article1 = dict(title="Doc Title 1", body="Doc Body 1")
#         self.article2 = dict(title="Doc Title 2", body="Doc Body 2")

#     def test_article_list_view(self):
#         self.assertEqual(reverse("article_list"), "/blog/")

#         Article.objects.create(**self.article1)
#         Article.objects.create(**self.article2)
#         response = self.client.get("/blog/")

#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, "article/list.html")
#         self.assertTemplateUsed(response, "theme.html")
#         self.assertContains(response, "<tr>", count=3)

#     def test_article_detail_view(self):
#         Article.objects.create(**self.article1)
#         self.assertEqual(reverse("article_detail", args="1"), "/article/1")
#         self.assertEqual(reverse("article_detail", args="2"), "/article/2")
#         response = self.client.get(reverse("article_detail", args="1"))
#         self.assertContains(response, "body")

#     def test_secure_add_view(self):

#         # Add without Login
#         response = self.client.post(reverse("article_add"), self.article1)
#         response = self.client.post(reverse("article_add"), self.article2)
#         self.assertEqual(response.status_code, 302)

#         # Login to add
#         self.assertEqual(response.url, "/accounts/login/?next=/article/add")
#         self.login()
#         response = self.client.post(reverse("article_add"), self.article1)
#         response = self.client.post(reverse("article_add"), self.article2)
#         self.assertEqual(response.status_code, 302)
#         response = self.client.get(response.url)
#         self.assertEqual(len(Article.objects.all()), 2)

#     def test_secure_edit_view(self):

#         # Edit without Login
#         response = Article.objects.create(**self.article1)
#         response = self.client.post(reverse("article_edit", args="1"), self.article2)
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(response.url, "/accounts/login/?next=/article/1/")

#         # Login to edit
#         self.login()
#         response = self.client.post(reverse("article_add"), self.article1)
#         response = self.client.post("/article/1/", self.article2)

#         self.assertEqual(response.status_code, 302)
#         response = self.client.get(response.url)
#         article = Article.objects.get(pk=1)

#         self.assertEqual(article.title, self.article2["title"])
#         self.assertEqual(article.body, self.article2["body"])

#     def test_secure_delete_view(self):
#         self.login()
#         Article.objects.create(**self.article1)
#         self.assertEqual(reverse("article_delete", args="1"), "/article/1/delete")
#         response = self.client.post("/article/1/delete")
#         self.assertEqual(len(Article.objects.all()), 0)

# def test_article_add_view(self):

#     # Add without Login
#     response = self.client.post(reverse("article_add"), self.article1)
#     response = self.client.post(reverse("article_add"), self.article2)
#     self.assertEqual(response.status_code, 302)
#     self.assertEqual(response.url, "/article/")
#     response = self.client.get(response.url)
#     self.assertEqual(len(Article.objects.all()), 2)

# def test_article_edit_view(self):
#     response = self.client.post(reverse("article_add"), self.article1)
#     response = self.client.post("/article/1/", self.article2)
#     self.assertEqual(response.status_code, 302)
#     response = self.client.get(response.url)
#     article = Article.objects.get(pk=1)

#     self.assertEqual(article.title, self.article2["title"])
#     self.assertEqual(article.body, self.article2["body"])

# def test_article_delete_view(self):
#     self.login()
#     Article.objects.create(**self.article1)
#     self.assertEqual(reverse("article_delete", args="1"), "/article/1/delete")
#     response = self.client.post("/article/1/delete")
#     self.assertEqual(len(Article.objects.all()), 0)
