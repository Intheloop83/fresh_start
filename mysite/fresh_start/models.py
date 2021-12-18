from django.db import models
from datetime import datetime
from django import forms

# Create your models here.


class ResourcePost(models.Model):
    title = models.CharField(max_length=50)
    thumbnail = models.URLField(null=True)
    featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    # def get_absolute_url(self):
    # return reverse('post-detail', kwargs={'pk: self.pk'})

class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=255)
    post_id = models.ForeignKey(ResourcePost, on_delete=models.CASCADE)

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    img_link = models.URLField()
    title = models.CharField(max_length=255)
    body = models.TextField()
    tags = models.ManyToManyField(Tag)