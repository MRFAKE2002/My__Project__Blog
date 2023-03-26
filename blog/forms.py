from django import forms

from .models import BlogPostComment

class BlogPostCommentForm(forms.Form):
    model = BlogPostComment
    fields = ['description', 'stars']

