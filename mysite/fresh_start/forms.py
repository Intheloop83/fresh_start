from django import forms


class ResourceForm(forms.Form):
    name = forms.CharField(label='Name/Organization', max_length=100)
    url = forms.URLField(label='Website')


class CommentForm(forms.Form):
    body = forms.CharField(label='Add Comment', max_length=100)
    # tag = forms.CharField(label='Add a Tag', max_length=100)
