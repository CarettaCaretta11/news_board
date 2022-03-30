from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes, name="api"),
    path("posts/create/", views.createPost),
    path("posts/", views.getPosts),
    path("post/<slug:link>/", views.getPost),
    path("post/<slug:link>/update/", views.PostRetrieveUpdateAPIView.as_view()),
    path("post/<slug:link>/upvote/", views.upvotePost),
    path("post/<slug:link>/delete/", views.PostDeleteAPIView.as_view()),
    path("comments/create/", views.createComment),
    path("comments/", views.getComments),
    path("comment/<str:pk>/", views.getComment),
    path("comment/<str:pk>/update/", views.CommentRetrieveUpdateAPIView.as_view()),
    path("comment/<str:pk>/delete/", views.CommentDeleteAPIView.as_view()),
]
