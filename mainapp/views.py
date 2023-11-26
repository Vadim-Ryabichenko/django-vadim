from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article, Comment

def mainpage(request):
    articles = Article.objects.all()
    return render(request, 'mainpage.html', {'articles' : articles})

def about_page(request):
    return render(request, 'about.html')

def articlepage(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = Comment.objects.all()
    return render(request, 'articlepage.html', {'article': article, 'comments': comments})

def article_comment(request, pk):
    return HttpResponse(f"Hello, it`s comment to {pk} article page")

def article_create(request):
    return render(request, 'articlecreate.html')

def article_update(request, pk):
    return HttpResponse(f"Hello, it`s page for updating {pk} article")

def article_delete(request, pk):
    return HttpResponse(f"Hello, it`s page for droping {pk} article")
