from django.contrib import admin

from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'is_active']
    
    list_filter = ['published', 'status', 'is_active']
    
    search_fields = ['title', 'content']
    
    ordering = ['status', 'is_active', 'published']
    
    prepopulated_fields = {'slug':['title']}


