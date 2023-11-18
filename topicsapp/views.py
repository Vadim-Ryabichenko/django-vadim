from django.shortcuts import render
from django.http import HttpResponse


def topics_page(request):
    return HttpResponse("Hello, it`s page for topics")

def topic_subscribe(request, topic_id):
    return HttpResponse(f"Hello, it`s page for subscribe {topic_id} topic ")

def topic_unsubscribe(request, topic_id):
    return HttpResponse(f"Hello, it`s page for unsubscribe {topic_id} topics")
