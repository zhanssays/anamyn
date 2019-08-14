from django.urls import path
from .views import CommentLike, DetailView, PostCreateView, PostListView, PostLike, PostComment, PostUpdate, PostDelete

app_name = 'post'

urlpatterns = [
    path("posts", PostListView.as_view(), name='post-list'),
    path("post-create", PostCreateView.as_view(), name='post-create'),

    path('post/<int:pk>/', DetailView.as_view(), name='detail'),
    path('post/<int:pk>/update/', PostUpdate.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='post-delete'),
    path('post/<int:pk>/comment/', PostComment.as_view(), name='post-comment'),
    path('post/<int:pk>/like/', PostLike.as_view(), name='post-like'),

    path('post/comment/<int:comment_pk>/like', CommentLike.as_view(), name='comment-like'),

]
