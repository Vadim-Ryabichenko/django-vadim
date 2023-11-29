from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article, Comment
from topicsapp.models import Topic
from django.shortcuts import redirect
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required


def mainpage(request):
    topics = Topic.objects.all()
    articles = Article.objects.all()
    return render(request, 'mainpage.html', {'topics' : topics, 'articles' : articles})


def about_page(request):
    return render(request, 'about.html')


def articlepage(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = Comment.objects.filter(article=article)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.user = request.user if request.user.is_authenticated else None
            comment.save()
            return redirect('articlepage', pk=article.pk)
    else:
        form = CommentForm()
        return render(request, 'articlepage.html', {'article': article, 'comments': comments, 'form' : form})


def article_comment(request, pk):
    return HttpResponse(f"Hello, it`s comment to {pk} article page")


@login_required(login_url='/accounts/login/')
def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            article.user = request.user if request.user.is_authenticated else None
            article.save()
            return redirect('articlepage', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'articlecreate.html', {'form': form})


def article_update(request, pk):
    return HttpResponse(f"Hello, it`s page for updating {pk} article")


def article_delete(request, pk):
    return HttpResponse(f"Hello, it`s page for droping {pk} article")

