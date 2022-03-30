from rest_framework.reverse import reverse
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Post, Comment


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "title",
            "link",
            "author",
            "upvotes",
            "updated",
            "created",
            "comments",
        ]


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
