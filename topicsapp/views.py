from django.shortcuts import render
from .models import Topic
from mainapp.models import Article
from django.views.generic import ListView, View


class TopicListView(ListView):
    model = Article
    template_name = 'topiclist.html'
    extra_context = {'topics' : Topic.objects.all()}


class TopicSubscribeView(View):
    def get(self, request, pk):
        topics = Topic.objects.filter(pk=pk)
        articles = Article.objects.filter(topics__id=pk)
        return render(request, 'art_list.html', {'topics': topics, 'articles': articles})


