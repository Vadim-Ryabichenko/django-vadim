from .models import Article, Comment
from django.shortcuts import redirect, render, get_object_or_404
from topicsapp.models import Topic
from .forms import ArticleForm, CommentForm, FindArticleForm
from django.views.generic import ListView, TemplateView, CreateView, DeleteView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin


class AboutView(TemplateView):
    template_name = "about.html"


class ArticleListView(ListView):
    model = Article
    template_name = 'mainpage.html'
    form_class = FindArticleForm
    http_method_names = ['get']
    extra_context = {'topics' : Topic.objects.all(), 'articles' : Article.objects.all(), 'art_list' : FindArticleForm()}
    success_url = '/'
    queryset = Article.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        if name := self.request.GET.get('name'):
            queryset = queryset.filter(name__icontains=name)
        return queryset


class ArticlePageView(LoginRequiredMixin, View):

    def get(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        comments = Comment.objects.filter(article=article)
        form = CommentForm()
        return render(request, 'articlepage.html', {'article': article, 'comments': comments, 'form': form})

    def post(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        comments = Comment.objects.filter(article=article)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.user = request.user if request.user.is_authenticated else None
            comment.save()
            return redirect('articlepage', pk=article.pk)
        return render(request, 'articlepage.html', {'article': article, 'comments': comments, 'form': form})
    

class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = 'articlecreate.html'
    http_method_names = ['get', 'post']
    form_class = ArticleForm
    success_url = '/'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form=form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'articleupdate.html'
    fields = ['text']

    def form_valid(self, form):
        comment = self.get_object()
        if comment.user == self.request.user:
            return super().form_valid(form)
        else: return redirect('mainpage')


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = '/'

