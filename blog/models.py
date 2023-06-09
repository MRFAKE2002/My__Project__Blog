from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth import get_user_model

from ckeditor.fields import RichTextField


class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)


class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, related_name="children", verbose_name=_('category_parent'))
    
    title = models.CharField(_('title'), max_length=200)
    
    slug = models.SlugField(_('slug'), unique=True, max_length=250)
    
    status = models.BooleanField(_('status'), default=True)

    position = models.IntegerField(_('position'))

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'
        ordering = ('parent__id', 'position')
    
    def __str__(self):
        return self.title

    object = CategoryManager()


# My manager class
class PostManager(models.Manager):
    def published(self):
        return self.filter(status = 'pu').order_by('published')


class BlogPost(models.Model):
    
    """
    This is the class for creating a new blog post.
    """
    
    STATUS_CHOICES = [
        ('dr', _('draft')),
        ('pu', _('published')),
    ]
    
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts', verbose_name=_('author'))
    
    title = models.CharField(_('title'), max_length=250)
    
    slug = models.SlugField(_('slug'), unique=True, max_length=250)

    category = models.ManyToManyField(Category, verbose_name=_('Category'), related_name="categories")
    
    content = RichTextField(_('content')) 
    
    image = models.ImageField(_('image'), upload_to='media')
    
    published = models.DateTimeField(_('published'), default = timezone.now())
    
    datetime_creation = models.DateTimeField(_('datetime_creation'), auto_now_add = True)
    
    datetime_modified = models.DateTimeField(_('datetime_modified'), auto_now = True)
    
    is_active = models.BooleanField(_('active'), default = True)
    
    status = models.CharField(_('status'), choices=STATUS_CHOICES, max_length=10)
    
    class Meta:
        verbose_name = _('Blog Post')
        verbose_name_plural = _('Blog Posts')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:post_details", args=[ self.pk ])

    def categories_Status_true(self):
        return self.category.filter(status=True)
    
    
    object = PostManager()
    
class BlogPostComment(models.Model):
    
    """
    This class is for creating a comment on a blog post.
    """
    
    STARS_CHOICES = [
        ('1', _("worst")),
        ('2', _("bad")),
        ('3', _("normal")),
        ('4', _("good")),
        ('5', _("perfect")),
    ]
    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_('User'), related_name='comments')
    
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, verbose_name=_('BlogPost'), related_name='comments')
    
    description = models.TextField(_('Description'))
    
    stars = models.CharField(_('Stars'), max_length=10, choices=STARS_CHOICES)
    
    is_active = models.BooleanField(_('is_active'), default=True)

    published = models.DateTimeField(_('published'), default = timezone.now())
    
    datetime_creation = models.DateTimeField(_('datetime_creation'), auto_now_add = True)
    
    datetime_modified = models.DateTimeField(_('datetime_modified'), auto_now = True)

    class Meta:
        verbose_name = _('Blog Post Comment')
        verbose_name_plural = _('Blog Post Comments')
    

    def __str__(self):
        return f'user:{self.user} / post:{self.post}'
    
    
    def get_absolute_url(self):
        return reverse('blog:post_details', args=[self.post.id])
    

