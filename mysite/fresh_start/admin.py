from django.contrib import admin
from .models import ResourcePost, Tag

# Register your models here.
admin.site.register(ResourcePost)
admin.site.register(Tag)
# admin.site.register(Comment)