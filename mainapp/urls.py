from .views import ArticleListView, AboutView, ArticleCreateView, ArticleDeleteView, ArticlePageView, BlogUpdateView
from django.urls import path


urlpatterns = [
    path('', ArticleListView.as_view(), name='mainpage'),
    path('about/', AboutView.as_view(), name='about'),
    path('article/<int:pk>/', ArticlePageView.as_view(), name='articlepage'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/update/', BlogUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]