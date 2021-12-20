from django.urls import path
from .views import ResourcePostListView, ResourcePostDetailView, ResourceCommentsView
from . import views

urlpatterns = [
    path('', views.home, name='fresh_start-home'),
    path('about/', views.about, name='fresh_start-about'),
    path('resources/', ResourcePostListView.as_view(),
         name='fresh_start-resources'),
    path('post/<pk>/', ResourcePostDetailView.as_view(), name='post-detail'),
    path('resources/resourcepost_detail/<int>', ResourceCommentsView.as_view(),
         name='fresh_start-resourcepost_detail'),
    path('addresource/', views.addresource, name='fresh_start-addresource'),
    path(r'^edit.html/', views.edit, name='edit')
]
