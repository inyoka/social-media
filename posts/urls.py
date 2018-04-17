from django.urls import path, include
from .views import PostList, CreatePost, UserPosts, PostDetail

app_name = 'posts'

urlpatterns = [
    path('', PostList.as_view(), name='all'),
    path('new/', CreatePost.as_view(), name='create'),
    path('by/<username>/', UserPosts.as_view(), name='for_user'),
    path('by/<username>/<int:pk>', PostDetail.as_view(), name='single')
    path('delete/<int:pk>/', views.DeletePost.as_view(),name='delete')
]
