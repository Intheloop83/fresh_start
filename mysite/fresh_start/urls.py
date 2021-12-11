from django.urls import path
from .views import ResourcePostListView, ResourcePostDetailView, ResourceCommentsView, ResourceCreateView, ResourceUpdateView
from . import views

urlpatterns = [
    path('', views.home, name='fresh_start-home'),
    path('about/', views.about, name='fresh_start-about'),
    path('resources/', ResourcePostListView.as_view(),
         name='fresh_start-resources'),
    path('post/<int:pk>/', ResourcePostDetailView.as_view(), name='post-detail'),
    path('post/new/', ResourceCreateView.as_view(), name='post-create'),
    path('resources/resourcepost_detail/<int>', ResourceCommentsView.as_view(),
         name='fresh_start-resourcepost_detail'),
    path('addresource/', views.addresource, name='fresh_start-addresource'),
    path('post/<int:pk>/update/', ResourceUpdateView.as_view(), name='post-update'),
    path('', views.add_resources, name='fresh_start-add_resources'),
]
