from django.contrib import admin

from .models import BlogPost, BlogPostComment

from jalali_date.admin import ModelAdminJalaliMixin


class CommentsInline(admin.TabularInline):
    model = BlogPostComment
    list_display = ['user', 'description', 'stars', 'is_active']
    extra = 0


@admin.register(BlogPost)
class BlogPostAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'is_active']
    
    list_filter = ['published', 'status', 'is_active']
    
    search_fields = ['title', 'content']
    
    ordering = ['status', 'is_active', 'published']
    
    prepopulated_fields = {'slug':['title']}
    
    inlines = [
    CommentsInline,
    ]



@admin.register(BlogPostComment)
class BlogPostCommentAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['user', 'post', 'stars', 'is_active']
    
    list_filter = ['published', 'is_active']
    
    search_fields = ['user', 'description']
    
    ordering = ['is_active', 'published']

