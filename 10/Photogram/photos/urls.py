
from django.urls import path

from .views_author import AuthorDeleteView, AuthorDetailView, AuthorHomeView, AuthorListView, AuthorCreateView, AuthorUpdateView


urlpatterns = [

    # Default
    path('',                              AuthorHomeView.as_view(), name='author_home'),

    # Author
    path('author/',                       AuthorListView.as_view(),    name='author_list'),
    path('author/<int:pk>',               AuthorDetailView.as_view(),  name='author_detail'),
    path('author/add',                    AuthorCreateView.as_view(),  name='author_add'),
    path('author/<int:pk>/',              AuthorUpdateView.as_view(),  name='author_edit'),
    path('author/<int:pk>/delete',        AuthorDeleteView.as_view(),  name='author_delete'),

]
