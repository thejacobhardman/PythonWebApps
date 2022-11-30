from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, RedirectView, TemplateView
from .models import Hero, Article, Photo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

#Superhero Views
class HeroListView(ListView):
    context_object_name = "hero_list"
    template_name = "hero/list.html"
    queryset = Hero.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['photo_list'] = Photo.objects.all()
        context['article_list'] = Article.objects.all()
        return context

class HeroDetailView(DetailView):
    template_name = "hero/detail.html"
    model = Hero

class HeroCreateView(LoginRequiredMixin, CreateView):
    template_name = "hero/add.html"
    model = Hero
    fields = "__all__"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class HeroUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "hero/edit.html"
    model = Hero
    fields = "__all__"

class HeroDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "hero/delete.html"
    model = Hero
    success_url = reverse_lazy('hero_list')

# Blog Views
class ArticleListView(ListView):
    template_name = 'blog/list.html'
    model = Article
    context_object_name = "articles"

class ArticleDetailView(DetailView):
    template_name = 'blog/detail.html'
    model = Article
    context_object_name = "article"

class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = 'blog/add.html'
    model = Article
    fields = "__all__"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleEditView(LoginRequiredMixin, UpdateView):
    template_name = 'blog/edit.html'
    model = Article
    fields = "__all__"

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'blog/delete.html'
    model = Article
    success_url = reverse_lazy('article_list')

# Account Views
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/account_add.html'

# Photo Views
class PhotoView(RedirectView):
    url = reverse_lazy('photo_list')

class PhotoListView(ListView):
    template_name = 'photo/list.html'
    model = Photo
    context_object_name = 'photos'

# class PhotoCarouselView(TemplateView):
#     template_name = 'photo/carousel.html'

#     def get_context_data(self, **kwargs):
#         photos = Author.get_me(self.request.user).photos
#         carousel = carousel_data(photos)
#         return dict(title='Carousel View', carousel=carousel)


# def carousel_data(photos):

#     def photo_data(id, image):
#         x = dict(image_url=f"/media/{image}", id=str(id), label=f"{image} {id}")
#         if id == 0:
#             x.update(active="active", aria='aria-current="true"')
#         return x

#     return [photo_data(id, photo.image) for id, photo in enumerate(photos)]

class PhotoDetailView(DetailView):
    template_name = 'photo/detail.html'
    model = Photo
    context_object_name = 'photo'

class PhotoCreateView(LoginRequiredMixin, CreateView):
    template_name = "photo/add.html"
    model = Photo
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "photo/edit.html"
    model = Photo
    fields = '__all__'

class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    template_name = 'photo/delete.html'
    success_url = reverse_lazy('photo_list')
