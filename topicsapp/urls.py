from .views import TopicListView, TopicSubscribeView
from django.urls import path


urlpatterns = [
    path('', TopicListView.as_view(), name = 'topiclist'),
    path('<int:pk>/subscribe/', TopicSubscribeView.as_view(), name = 'art_list'),
]