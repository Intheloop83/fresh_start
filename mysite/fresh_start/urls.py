from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='fresh_start-home'),
    path('about/', views.about, name='fresh_start-about'),
    path("", include("add_resources.urls")),
    path("comments/", include("comment.urls")),
    path("admin/", admin.site.urls),
]