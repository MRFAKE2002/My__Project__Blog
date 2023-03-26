from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import BlogPost, BlogPostComment
from .forms import BlogPostCommentForm

class PostListView(generic.ListView):
    # model = BlogPost
    queryset = BlogPost.objects.filter(status='pu').order_by('published')
    
    template_name = 'blog/post_list.html'
    
    context_object_name = 'posts'


class PostDetailsView(generic.DeleteView):
    model = BlogPost
    
    template_name = 'blog/post_details.html'
    
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['comment_form'] = BlogPostCommentForm
        
        return context
    

class BlogPostCommentView(generic.CreateView):
    model = BlogPostComment
    
    form = BlogPostCommentForm
    
    def form_valid(self, form):
        form = form.save(commit=False)
        
        form.user = self.request.user
        
        post_id = int(self.kwargs['post_id'])
        
        form.post = get_object_or_404(BlogPost, id=post_id)
        
        return form.save()

