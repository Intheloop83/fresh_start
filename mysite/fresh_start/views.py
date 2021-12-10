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
    if request.method == 'GET':
        # create empty form
        form = EditorForm()
        return render(request=request, template_name='create.html', context={'form': form})
    if request.method == 'POST':
        # capture POST data as EditorForm instance
        form = EditorForm(request.POST)
        # validate form
        if form.is_valid():
            # get cleaned data from form
            title = form.cleaned_data['title']
            img_link = form.cleaned_data['img_link']
            body = form.cleaned_data['body']
            tags = form.cleaned_data['tags']
            post = Post.objects.create(
                title=title, body=body, img_link=img_link)
            # set cleaned tags to ManyRelatedManager object
            post.tags.set(tags)
        # redirect to 'addresources.html/'
        return HttpResponseRedirect(reverse('resourcepostl.html'))


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
