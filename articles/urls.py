# urls.py
from django.urls import path
from .views import (
    article_list_view, article_detail_view, article_search_view,
    article_create_view, article_edit_view, article_delete_view
)

urlpatterns = [
    path('', article_list_view, name='article-list'),
    path('<int:id>/', article_detail_view, name='article-detail'),
    path('search/', article_search_view, name='article-search'),
    path('create/', article_create_view, name='article-create'),
    path('edit/<int:id>/', article_edit_view, name='article-edit'),
    path('delete/<int:id>/', article_delete_view, name='article-de')
    ]