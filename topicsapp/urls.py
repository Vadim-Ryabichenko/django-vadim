from .views import topics_page, topic_subscribe, topic_unsubscribe
from django.urls import path


urlpatterns = [
    path('', topics_page),
    path('<int:pk>/subscribe/', topic_subscribe, name = 'art_list'),
    path('<int:topic_id>/unsubscribe/', topic_unsubscribe),
]