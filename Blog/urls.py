from django.urls import path
from .views import (CreatePost, DeletePost, UpdatePost, 
ListPost, ShowPost,SaveLike, ShowLike, CreateComment,DeleteComment,
UpdateComment, ListComment, ShowComment)


app_name = "Blog"

urlpatterns = [
    path('list/', ListPost.as_view(),
    name="list-post"),

    path('show/<int:pk>/', ShowPost.as_view(),
    name="show-post"),

    path('create/', CreatePost.as_view(),
    name="create-post"),

    path('delete/<int:pk>/', DeletePost.as_view(),
    name="delete-post"),

    path('update/<int:pk>/', UpdatePost.as_view(),
    name="update-post"),

    path('like/save/', SaveLike.as_view(),
    name="save-like"),

    path('like/show/<int:pk>/', ShowLike.as_view(),
    name="show-like"),

    path('comment/list/', ListComment.as_view(),
    name="list-comment"),

    path('comment/show/<int:pk>/', ShowComment.as_view(),
    name="show-comment"),

    path('comment/create/', CreateComment.as_view(),
    name="create-comment"),

    path('comment/update/<int:pk>/', UpdateComment.as_view(),
    name="update-comment"),

    path('comment/delete/<int:pk>/', DeleteComment.as_view(),
    name="delete-comment"),
]