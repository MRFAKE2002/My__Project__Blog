from django.urls import path 

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetailsView.as_view(), name='post_details'),
    path('comment/<int:post_id>/', views.BlogPostCommentView.as_view(), name='comment_create'),
]
