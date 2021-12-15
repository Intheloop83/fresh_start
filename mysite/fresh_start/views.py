from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ResourcePost
from .forms import ResourceForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def home(request):
    return render(request, 'fresh_start/home.html')


def about(request):
    return render(request, 'fresh_start/about.html', {'title': 'About'})


def resources(request):
    context = {
        'posts': ResourcePost.objects.all()
    }
    return render(request, 'fresh_start/resources.html', {'title': 'Resources'}, context)


def resourcepost_detail(request, resourcenumber):
    if request.method == 'GET':
        resourcepost = ResourcePost.objects.get(pk=resourcenumber)

    return render(request, 'fresh_start/resourcepost_detail.html', context={'resource': resourcepost})


def addresource(request):
    if request.method == 'GET':
        form = ResourceForm()
        return render(request, 'fresh_start/addresource.html', context={'form': form})
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        print(form)
        if form.is_valid():
            # get cleaned data from form
            name = form.cleaned_data['name']
            url = form.cleaned_data['url']
            resource = ResourcePost.objects.create(title=name, thumbnail=url)
            return HttpResponseRedirect(reverse('fresh_start-resources'))

            """ borough1 = form.cleaned_data['Brooklyn']
            #borough2 = form.cleaned_data['Bronx']
            borough3 = form.cleaned_data['Manhattan']
            borough4 = form.cleaned_data['Queens']
            #borough5 = form.cleaned_data['Staten Island']
            #phonenumber = form.cleaned_data['phonenumber'] """

# def create(request):
# def create_resource(request):
    # form =
    # if request.method == 'GET':
    # create empty form
    #form = ResourceForm()
    # return render(request=request, template_name='create.html', context={'form': form})
    # if request.method == 'POST':
    # capture POST data as EditorForm instance
    #form = resourceform(request.POST)
    # validate form

    # if form.is_valid():
    # get cleaned data from form
    #resource1 = form.cleaned_data['resource1']
    #resource2 = form.cleaned_data['resource2']
    #borough1 = form.cleaned_data['Brooklyn']
    ##borough2 = form.cleaned_data['Bronx']
    #borough3 = form.cleaned_data['Manhattan']
    #borough4 = form.cleaned_data['Queens']
    #borough5 = form.cleaned_data['Staten Island']
    #phonenumber = form.cleaned_data['phonenumber']

    # post = Post.objects.create(
    # resource1=resource1, resource2=resource2, borough1=borough1)
    # set cleaned tags to ManyRelatedManager object
    # post.tags.set(tags)
    # redirect to 'addresources.html/'
    # return HttpResponseRedirect(reverse('/resources/'))


class ResourcePostListView(ListView):
    model = ResourcePost
    template_name = 'fresh_start/resources.html'
    context_object_name = 'posts'
    ordering = ['-date_created']


class ResourcePostDetailView(DetailView):
    model = ResourcePost


class ResourceCommentsView(ListView):
    model = ResourcePost
    template_name = 'fresh_start/resourcepost_detail.html'
