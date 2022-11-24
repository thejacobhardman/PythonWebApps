from django.urls import path, include
from hero.views import *
from django.contrib import admin

urlpatterns =  [
    # Superhero urls
    path('', HeroListView.as_view(), name='hero_list'),
    path('<int:pk>', HeroDetailView.as_view(), name='hero_detail'),
    path('add', HeroCreateView.as_view(), name='hero_add'),
    path('<int:pk>/', HeroUpdateView.as_view(), name='hero_edit'),
    path('<int:pk>/delete', HeroDeleteView.as_view(), name='hero_delete'),

    # Blog urls
    path('blog/', ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('article/add', ArticleCreateView.as_view(), name='article/add'),
    path('article/<int:pk>/', ArticleEditView.as_view(), name='article_edit'),
    path('article/<int:pk>/delete', ArticleDeleteView.as_view(), name='article_delete'),

    # Accounts
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),

    # Admin
    path('admin/', admin.site.urls),
]
