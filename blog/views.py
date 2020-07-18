from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Post, AboutContent
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class BlogPageView(ListView):
    queryset = Post.objects.order_by('-id')
    model = Post
    template_name = 'home.html'


#    def get_queryset(self, *args, **kwargs):
#        qs = super(Post, self).get_queryset(*args, **kwargs)
#        qs = qs.order_by("-id")
#        return qs

class AboutPageView(ListView):
    model = AboutContent
    template_name = 'about.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'content', 'author', 'date_posted']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'content']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('main-home')
# Create your views here.
