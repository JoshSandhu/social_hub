from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('create_post/', views.CreatePost.as_view(), name='create_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('dislike/<slug:slug>', views.PostDislike.as_view(), name='post_dislike'),
    path('user_posts', views.user_posts, name='user_posts'),
    path('delete/<post_id>', views.delete_post, name='delete_post'),
]