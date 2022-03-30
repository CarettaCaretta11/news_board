from rest_framework.response import Response
from rest_framework import generics
from rest_framework.status import HTTP_201_CREATED
from rest_framework.decorators import api_view
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.shortcuts import render
from django.db.models import F


def home(request):
    return render(request, "base/home.html")


@api_view(["GET"])
def getRoutes(request):
    routes = [
        "GET /api/",
        "GET /api/posts/",
        "POST /api/post/<slug:link>/",
        "POST /api/posts/create/",
        "PUT /api/post/<slug:link>/update/",
        "GET /api/post/<slug:link>/upvote/",
        "DELETE /api/post/<slug:link>/delete/",
        "GET /api/comments/",
        "GET /api/comment/<str:pk>/",
        "POST /api/comments/create/",
        "PUT /api/comment/<str:pk>/update/",
        "DELETE /api/comment/<str:pk>/delete/",
    ]
    return Response(routes)


@api_view(["GET"])
def getPosts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getPost(request, link):
    if Post.objects.filter(link=link):
        post = Post.objects.get(link=link)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    else:
        return Response({"msg": "No such post."})


@api_view(["GET", "POST"])
def createPost(request):
    if request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if Post.objects.filter(title=request.data["title"]).exists():
            return Response({"msg": "A post with this title already exists."})
        elif serializer.is_valid():
            serializer.save()
            res = {"msg": "New post created successfully."}
            return Response(res, status=HTTP_201_CREATED)
        else:
            return Response({"msg": "An error occured."})
    else:
        return Response(
            {"msg": "Write down the necessary attributes to create a new post"}
        )


class PostRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = "link"
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@api_view(["GET"])
def upvotePost(request, link):
    if Post.objects.filter(link=link):
        post = Post.objects.get(link=link)
        post.upvotes = F("upvotes") + 1
        post.save()
        return Response({"msg": "Post upvoted successfully."})
    else:
        return Response({"msg": "No such post."})


class PostDeleteAPIView(generics.DestroyAPIView):
    lookup_field = "link"
    queryset = Post.objects.all()


@api_view(["GET"])
def getComments(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getComment(request, pk):
    if Comment.objects.filter(pk=pk):
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    else:
        return Response({"msg": "No such comment."})


@api_view(["GET", "POST"])
def createComment(request):
    if request.method == "POST":
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {"msg": "New comment created successfully."}
            return Response(res, status=HTTP_201_CREATED)
        else:
            return Response({"msg": "An error occured."})
    else:
        return Response(
            {"msg": "Write down the necessary attributes to create a new comment."}
        )


class CommentRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = "pk"
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDeleteAPIView(generics.DestroyAPIView):
    lookup_field = "pk"
    queryset = Comment.objects.all()
