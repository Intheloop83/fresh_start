from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ResourcePost


def home(request):
    return render(request, 'fresh_start/home.html')


def about(request):
    return render(request, 'fresh_start/about.html', {'title': 'About'})


def resources(request):
    context = {
        'posts': ResourcePost.objects.all()
    }
    return render(request, 'fresh_start/resources.html', {'title': 'Resources'}, context)


class ResourcePostListView(ListView):
    model = ResourcePost
    template_name = 'fresh_start/resources.html'


#class ResourcePostListView(ListView):
 #   model = ResourcePost
  #  template_name = 'fresh_start/resources.html'
   # context_object_name = 'posts'
    # ordering = ['-date_posted']

