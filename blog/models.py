from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth import get_user_model

class BlogPost(models.Model):
    
    STATUS_CHOICES = [
        ('dr', _('draft')),
        ('pu', _('published')),
    ]
    
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts', verbose_name=_('author'))
    
    title = models.CharField(_('title'), max_length=250)
    
    slug = models.SlugField(_('slug'), unique=True, max_length=250)
    
    content = models.TextField(_('content'))
    
    image = models.ImageField(_('image'), upload_to='media')
    
    published = models.DateTimeField(_('published'), default = timezone.now())
    
    datetime_creation = models.DateTimeField(_('datetime_creation'), auto_now_add = True)
    
    datetime_modified = models.DateTimeField(_('datetime_modified'), auto_now = True)
    
    is_active = models.BooleanField(_('active'), default = True)
    
    status = models.CharField(_('status'), choices=STATUS_CHOICES, max_length=10)
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = _('Blog Post')
        verbose_name_plural = _('Blog Posts')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:post_details", args=[ self.pk ])

    