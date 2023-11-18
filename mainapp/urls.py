from .views import main, about_page, article_page, article_comment, article_create, article_update, article_delete
from django.urls import path


urlpatterns = [
    path('', main),
    path('about/', about_page),
    path('article/<int:article_id>/', article_page),
    path('article/<int:article_id>/comment/', article_comment),
    path('create/', article_create),
    path('article/<int:article_id>/update/', article_update),
    path('article/<int:article_id>/delete/', article_delete),
]