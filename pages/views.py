from django.shortcuts import render
from django.views import generic

from blog.models import BlogPost

class HomeView(generic.ListView):
    model = BlogPost
    
    template_name = 'home.html'

    context_object_name = 'posts'


class ContactUsView(generic.TemplateView):
    template_name = 'pages/contact_us.html'

