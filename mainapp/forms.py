from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('name', 'text', 'topics')


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('text', )


class FindArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('name', )
        
   