from django import forms
from .models import Tag


class ResourceForm(forms.Form):
    name = forms.CharField(label='Organization/Name', max_length=100)
    url = forms.URLField(label='Website')

class EditorForm(forms.Form):
    title = forms.CharField(max_length=255, required=True)
    img_link = forms.URLField(required=True)
    body = forms.CharField(widget=forms.Textarea, required=True)
    # create tag choices for MultipleChoiceField
    choices = []
    for tag in Tag.objects.all():
        choices.append((tag.tag_id, tag.name))
    tags = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=choices, required=True)