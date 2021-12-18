from django import forms
from .models import Tag


class ResourceForm(forms.Form):
    name = forms.CharField(label='Organization/Name', max_length=100)
    url = forms.URLField(label='Website')

class EditorForm(forms.Form):
    title = forms.CharField(max_length=255)
    img_link = forms.URLField()
    body = forms.CharField(widget=forms.Textarea)
    # create tag choices for MultipleChoiceField
    choices = []
    for tag in tag.objects.all():
        choices.append((tag.tag_id, tag.name))
    tags = forms.MultipleChoiceField(widget=forms.CheckboxSelectMiltiple, choices=choices)