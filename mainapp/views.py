from django.shortcuts import render
from django.http import HttpResponse


def mainpage(request):
    return render(request, 'mainpage.html')

def about_page(request):
    return render(request, 'about.html')

def articlepage(request):
    return render(request, 'articlepage.html')

def article_comment(request, article_id):
    return HttpResponse(f"Hello, it`s comment to {article_id} article page")

def article_create(request):
    return render(request, 'articlecreate.html')

def article_update(request, article_id):
    return HttpResponse(f"Hello, it`s page for updating {article_id} article")

def article_delete(request, article_id):
    return HttpResponse(f"Hello, it`s page for droping {article_id} article")