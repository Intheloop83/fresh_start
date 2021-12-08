from django.shortcuts import render


def home(request):
    return render(request, 'fresh_start/home.html')


def about(request):
    return render(request, 'fresh_start/about.html', {'title': 'About'})


def add_resources(request):
    return render(request, 'fresh_start/add_reources.html', {'title': 'Add Resources'})


def comments(request):
    return render(request, 'fresh_start/comments.html', {'title': 'Comments'})