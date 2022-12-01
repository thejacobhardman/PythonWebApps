from django.urls import path, include
from hero.views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

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

    # Comment urls
    path('comments/', CommentListView.as_view(), name='comment_list'),
    path('comment/<int:pk>', CommentDetailView.as_view(), name='comment_detail'),
    path('comment/add', CommentCreateView.as_view(), name='comment/add'),
    path('comment/<int:pk>/', CommentEditView.as_view(), name='comment_edit'),
    path('comment/<int:pk>/delete', CommentDeleteView.as_view(), name='comment_delete'),

    # Photo
    path('photo/', PhotoListView.as_view(), name='photo_list'),
    path('photo/<int:pk>', PhotoDetailView.as_view(), name='photo_detail'),
    path('photo/add', PhotoCreateView.as_view(), name='photo_add'),
    path('photo/<int:pk>/', PhotoUpdateView.as_view(), name='photo_edit'),
    path('photo/<int:pk>/delete', PhotoDeleteView.as_view(), name='photo_delete'),

    # Accounts
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),

    # Admin
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
