# urls.py
from django.urls import path
from .views import announcements_list_view,announcement_detail_view,announcement_search_view,announcement_delete_view


urlpatterns = [
    path('', announcements_list_view, name='announcements-list'),
    path('<int:id>/', announcement_detail_view, name='announcement-detail'),
    path('search/', announcement_search_view, name='announcement-search'),
    path('delete/<int:id>/', announcement_delete_view, name='announcement-delete'),
]