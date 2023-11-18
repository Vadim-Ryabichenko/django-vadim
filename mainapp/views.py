from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return HttpResponse("Hello, it`s base page")

def about_page(request):
    return HttpResponse("Hello, it`s page about")

def article_page(request, article_id):
    return HttpResponse(f"Hello, it`s {article_id} article page")

def article_comment(request, article_id):
    return HttpResponse(f"Hello, it`s comment to {article_id} article page")

def article_create(request):
    return HttpResponse(f"Hello, it`s page for creating article")

def article_update(request, article_id):
    return HttpResponse(f"Hello, it`s page for updating {article_id} article")

def article_delete(request, article_id):
    return HttpResponse(f"Hello, it`s page for droping {article_id} article")