from .models import Article, Comment
from django.shortcuts import redirect, render, get_object_or_404
from topicsapp.models import Topic
from .forms import ArticleForm, CommentForm, FindArticleForm
from django.views.generic import ListView, TemplateView, CreateView, DeleteView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache


class AboutView(TemplateView):
    template_name = "about.html"


class ArticleListView(ListView):
    model = Article
    template_name = 'mainpage.html'
    form_class = FindArticleForm
    http_method_names = ['get']
    extra_context = {'topics' : Topic.objects.all(), 'articles' : Article.objects.all(), 'art_list_form': FindArticleForm()}
    success_url = '/'
    queryset = Article.objects.all()
    counter = 1 

    def get(self, request, *args, **kwargs):
        count = request.session.get('page_count', 0)
        count += 1
        if count % 4 == 0:
            self.extra_context['message'] = 'You have visited this page 4 times!'
        else:
            self.extra_context.pop('message', None)
        request.session['page_count'] = count
        count_10 = cache.get('page_count_10', 0)
        count_10 += 1
        cache.set('page_count_10', count_10)
        if count_10 % 10 == 0:
            self.extra_context['message_10'] = 'You are the tenth visitor!'
        else:
            self.extra_context.pop('message_10', None)
        return super().get(request, *args, **kwargs)

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
            comment.user = request.user 
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

