from .views import topics_page, topic_subscribe, topic_unsubscribe
from django.urls import path


urlpatterns = [
    path('', topics_page),
    path('<int:topic_id>/subscribe/', topic_subscribe),
    path('<int:topic_id>/unsubscribe/', topic_unsubscribe),
]