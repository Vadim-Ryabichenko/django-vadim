from .views import mainpage, about_page, articlepage, article_comment, article_create, article_update, article_delete
from django.urls import path


urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('about/', about_page, name='about'),
    path('article/', articlepage, name='articlepage'),
    path('article/<int:article_id>/comment/', article_comment),
    path('create/', article_create, name='article_create'),
    path('article/<int:article_id>/update/', article_update),
    path('article/<int:article_id>/delete/', article_delete),
]