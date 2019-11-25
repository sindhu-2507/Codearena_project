from django.urls import path
from .views import PostListView, PostCreateView
from .views import FriendCreateView, FriendListView
from . import views

urlpatterns = [
	path('', views.home, name='main'),
    path('friends/', FriendListView.as_view(), name='blog-home'),
    path('post/', PostListView.as_view(), name='blog-about'),
    path('friends/new/', FriendCreateView.as_view(), name='friend-create'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    #path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    #path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
   # path('about/', views.about, name='blog-about'),
]