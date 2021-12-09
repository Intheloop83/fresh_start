from django.urls import path
from .views import ResourcePostListView, ResourcePostDetailView
from . import views

urlpatterns = [
    path('', views.home, name='fresh_start-home'),
    path('about/', views.about, name='fresh_start-about'),
    path('resources/', ResourcePostListView.as_view(),
         name='fresh_start-resources'),
    path('post/<pk>/', ResourcePostDetailView.as_view(), name='post-detail'),
    path('resourcecom/', views.about, name='fresh_start-resourcecom'),



]
