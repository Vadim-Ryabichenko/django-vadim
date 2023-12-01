from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic
from mainapp.models import Article


def topics_page(request):
    return HttpResponse("Hello, it`s page for topics")

def topic_subscribe(request, pk):
    topics = Topic.objects.filter(pk=pk)
    articles = Article.objects.filter(topics__id = pk)
    return render(request, 'art_list.html', {'topics' : topics, 'articles' : articles})

def topic_unsubscribe(request, topic_id):
    return HttpResponse(f"Hello, it`s page for unsubscribe {topic_id} topics")
