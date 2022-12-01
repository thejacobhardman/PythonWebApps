from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User

def get_upload(instance, filename):
    return f'images/{filename}'

class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to=get_upload)
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, default="None")

    def __str__(self):
        return f'{self.pk} - {self.title}'

    def get_absolute_url(self):
        return reverse_lazy('photo_detail', args=[str(self.id)])

class Hero(models.Model):
    name = models.CharField(max_length=200, default="None")
    identity = models.CharField(max_length=200, default="None")
    description = models.TextField(default="None")
    image = models.ForeignKey(Photo, on_delete=models.CASCADE, null=True, blank=True)
    strengths = models.CharField(max_length=200, default="None")
    weaknesses = models.CharField(max_length=200, default="None")
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, default="None")

    def __str__(self):
        return self.identity

    def get_absolute_url(self):
        return reverse_lazy('hero_list')

class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, default="None")
    
    @property
    def comments(self):
        return Comment.objects.filter(article=self)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('article_list')

class Comment(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, default="None")
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse_lazy('comment_list')
