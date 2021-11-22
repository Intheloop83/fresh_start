from django.shortcuts import render


def home(request):
    return render(request, 'fresh_start/home.html')


def about(request):
    return render(request, 'fresh_start/about.html', {'title': 'About'})