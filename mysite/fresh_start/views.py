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


def resourcepost_detail(request, resourcenumber):
    if request.method == 'GET':
        resourcepost = ResourcePost.objects.get(pk=resourcenumber)

    return render(request, 'fresh_start/resourcepost_detail.html', context={'resource': resourcepost})


def addresource(request):
    return render(request, 'fresh_start/addresource.html')


# def create(request):
    # if request.method == 'GET':
    # create empty form
    # form = EditForm()
    # return render(request=request, template_name='create.html', context={'form': form})
    # if request.method == 'POST':
    # capture POST data as EditorForm instance
    #form = resourceform(request.POST)
    # validate form
    # if form.is_valid():
    # get cleaned data from form
    #resource1 = form.cleaned_data['resource']
    #resource2 = form.cleaned_data['resource']
    #borough1 = form.cleaned_data['Brooklyn']
    ##borough2 = form.cleaned_data['Bronx']
    #borough3 = form.cleaned_data['Manhattan']
    #borough4 = form.cleaned_data['Queens']
    #borough5 = form.cleaned_data['Staten Island']
    #phonenumber = form.cleaned_data['phonenumber']

    # post = Post.objects.create(
    # title=title, body=body, img_link=img_li)
    # set cleaned tags to ManyRelatedManager object
    # post.tags.set(tags)
    # redirect to 'addresources.html/'
    # return HttpResponseRedirect(reverse('resources.html'))


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
