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
