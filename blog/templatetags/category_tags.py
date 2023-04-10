from django import template
from django.utils.translation import gettext_lazy as _

from ..models import Category

register = template.Library()

@register.simple_tag
def site_name(default_name=_(" My Django Blog ")):
    """
    This is a function that returns the name of the site. 
    """
    return default_name


@register.inclusion_tag("header.html")
def categories_title():
    """
    This is a function that returns the title of the categories in header.html .  
    """
    # categories_info = Category.objects.filter(status=True)
    
    return {
        "categories_info":  Category.objects.filter(status=True),
    }
