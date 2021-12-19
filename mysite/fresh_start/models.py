from django.db import models
from datetime import datetime
from django import forms

# Create your models here.


class ResourcePost(models.Model):
    title = models.CharField(max_length=50)
    thumbnail = models.URLField(null=True)
    featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now, blank=True)


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    body = models.CharField(max_length=255)
    post_id = models.ForeignKey(ResourcePost, on_delete=models.CASCADE)


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    # def get_absolute_url(self):
    # return reverse('post-detail', kwargs={'pk: self.pk'})
