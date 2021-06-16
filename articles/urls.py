from django.urls import path
from .views import (
    ArticleListView,
    ArticleDeleteView,
    ArticleDetailView,
    ArticleEditView,
    ArticleCreateView)

# 127.0.0.1:8000/articles/ <--this is all implied, that's why it's an empty string

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('<int:pk>/edit/', ArticleEditView.as_view(), name='article_edit'),
    path('new/', ArticleCreateView.as_view(), name='article_new')
]