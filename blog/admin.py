from django.contrib import admin

from .models import Category, BlogPost, BlogPostComment

from jalali_date.admin import ModelAdminJalaliMixin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['position', 'title', 'status']
    
    list_filter = ['status']
    
    search_fields = ['title', 'slug']
    
    ordering = ['position']
    
    prepopulated_fields = {'slug':['title']}


class CommentsInline(ModelAdminJalaliMixin, admin.TabularInline):
    model = BlogPostComment
    list_display = ['user', 'description', 'stars', 'is_active']
    extra = 0


@admin.register(BlogPost)
class BlogPostAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'string_category', 'is_active']
    
    list_filter = ['published', 'status', 'is_active']
    
    search_fields = ['title', 'content']
    
    ordering = ['status', 'is_active', 'published']
    
    prepopulated_fields = {'slug':['title']}
    
    inlines = [
        CommentsInline,
    ]


    def string_category(self, object):
        return " , ".join([category.title for category in object.category.all()])



@admin.register(BlogPostComment)
class BlogPostCommentAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['user', 'post', 'stars', 'is_active']
    
    list_filter = ['published', 'is_active']
    
    search_fields = ['user', 'description']
    
    ordering = ['is_active', 'published']

