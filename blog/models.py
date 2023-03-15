from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.shortcuts import reverse


class BlogPost(models.Model):
    
    STATUS_CHOICES = [
        ('dr', 'draft'),
        ('pu', 'published'),
    ]
    
    title = models.CharField(_('title'), max_length=250)
    
    content = models.TextField(_('content'))
    
    published = models.DateTimeField(_('published'), default = timezone.now())
    
    datetime_creation = models.DateTimeField(_('datetime_creation'), auto_now_add = True)
    
    datetime_modified = models.DateTimeField(_('datetime_modified'), auto_now = True)
    
    is_active = models.BooleanField(_('active'), default = True)
    
    status = models.CharField(_('status'), choices=STATUS_CHOICES, max_length=10)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_details", kwargs={"pk": self.pk})

    