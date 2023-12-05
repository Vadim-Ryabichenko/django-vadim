from django.db import models
from topicsapp.models import Topic
from django.urls import reverse


class Article(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    topics = models.ManyToManyField(Topic)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return f"Article_name is ~{self.name}~"

    def get_absolute_url(self):
        return reverse("article_update", kwargs={'pk': self.pk})

class Comment(models.Model):
    create_at = models.DateField(auto_now_add=True)
    text = models.TextField(null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null = True, blank = True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return f"Comment created {self.create_at}, {self.text[:15]}"
    
