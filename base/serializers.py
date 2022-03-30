from rest_framework.reverse import reverse
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Post, Comment


class PostSerializer(ModelSerializer):
    comments = serializers.SerializerMethodField()
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
    def get_comments(self, obj):
        return [x.content for x in Comment.objects.filter(post=obj)]


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
