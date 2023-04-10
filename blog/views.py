from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.urls import reverse_lazy

from .models import BlogPost, BlogPostComment, Category
from .forms import BlogPostCommentForm

class PostListView(generic.ListView):
    # model = BlogPost
    queryset = BlogPost.objects.filter(status='pu').order_by('published')
    
    template_name = 'blog/post_list.html'
    
    context_object_name = 'posts'


class PostDetailsView(generic.DetailView):
    model = BlogPost
    
    template_name = 'blog/post_details.html'
    
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['comment_form'] = BlogPostCommentForm
        
        return context
    

class BlogPostCommentView(generic.CreateView):
    model = BlogPostComment
    
    form_class = BlogPostCommentForm
    
    # def get_success_url(self) -> str:
    #     return reverse('blog:post_list')
    
            
    def form_valid(self, form):
        comment = form.save(commit=False)
        
        comment.user = self.request.user
        
        post_id = int(self.kwargs['post_id'])
        
        post = get_object_or_404(BlogPost, id=post_id)
        
        comment.post = post
                
        return super().form_valid(form)


# class CategoriesPostListView(generic.ListView):
    
#     model = Category
    
#     template_name = "blog/categories_post_list.html"
    
#     context_object_name = "category_posts"

def categories_post_list(request, slug):
    context = {
        "categories_posts": get_object_or_404(Category, slug=slug, status=True) 
    }
    
    return render(request, "blog/categories_post_list.html", context)