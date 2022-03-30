from django.core.management.base import BaseCommand, CommandError
from base.models import Post

class Command(BaseCommand):
    
    def handle(self, *args, **kwargs):
        for post in Post.objects.all():
            post.upvotes = 0
            post.save()