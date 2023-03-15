from django.shortcuts import render
from django.views import generic

from .models import BlogPost

class PostListView(generic.ListView):
    # model = BlogPost
    queryset = BlogPost.objects.filter({'status':'pu', 'is_active':'True'}).order_by('published')
    
    template_name = 'blog/post_list.html'
    
    context_object_name = 'posts'

