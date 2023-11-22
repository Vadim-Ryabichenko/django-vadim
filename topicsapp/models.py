from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=255, null=True, blank=True)
    user = models.ManyToManyField("auth.User")

    def __str__(self):
        return f"Topic_name is ~{self.name}~"
