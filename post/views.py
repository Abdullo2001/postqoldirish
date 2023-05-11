from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView
from .models import Post
# class HomePageView(TemplateView):
#     template_name='home.html'

class AboutPageView(TemplateView):
    template_name='about.html'

# Create your views here.
class PostDetailView(DetailView):
    model=Post
    template_name='post_detail.html'

class HomePageView(ListView):
    model=Post
    template_name='home.html'

class PostCreateView(CreateView):
    model=Post
    template_name='post_create.html'
    fields=['title','author','body']

class PostUpdateView(UpdateView):
    model=Post
    template_name='post_update.html'
    fields=['title','body']