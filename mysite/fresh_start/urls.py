from django.urls import path
from .views import ResourcePostListView
from . import views

urlpatterns = [
    path('', views.home, name='fresh_start-home'),
    path('about/', views.about, name='fresh_start-about'),
    path('resources/', ResourcePostListView.as_view(), name='fresh_start-resources'),
]
