from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    link = models.SlugField(null=True, blank=True)
    upvotes = models.IntegerField()
    author = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return self.link

    def save(self, *args, **kwargs):
        self.link = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    author = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments", null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return self.content[:20]
