from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Hero
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

class HeroListView(ListView):
    template_name = "hero/list.html"
    model = Hero

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

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/account_add.html'
