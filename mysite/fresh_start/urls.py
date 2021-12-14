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
    # path('resources/create_resource/', views.create_resource name='fresh_start-create_resource'),
]

""" <label for="name">Name/Organization:</label><br>
    <input type="text" id="name" name="name"><br>
    <label for="resource">Type of Resource:</label><br>
    <input type="checkbox" id="resource1" name="resource1" value="Food">
    <label for="resource1"> Food</label><br>
    <input type="checkbox" id="resource2" name="resource2" value="Other">
    <label for="resource2"> Other</label><br>
    <label for="name">If you have selected other, please specify your resource below (Examples: Housing,
        Employment...):</label><br>
    <input type="text" id="other" name="other"><br>
    <label for="webaddress">Website Address:</label><br>
    <input type="text" id="webaddress" name="webaddress"><br>
    <label for="name">Borough:</label><br>
    <input type="checkbox" id="borough1" name="borough1" value="Brooklyn">
    <label for="borough1"> Brooklyn</label><br>
    <input type="checkbox" id="borough2" name="borough2" value="Bronx">
    <label for="borough2"> Bronx</label><br>
    <input type="checkbox" id="borough3" name="borough3" value="Manhattan">
    <label for="borough3"> Manhattan</label><br>
    <input type="checkbox" id="borough4" name="borough4" value="Queens">
    <label for="borough4"> Queens</label><br>
    <input type="checkbox" id="borough5" name="borough5" value="Staten Island">
    <label for="borough5"> Staten Island</label><br>
    <label for="name">Phone Number:</label><br>
    <input type="text" id="phonenumber" name="phone number"><br> """
