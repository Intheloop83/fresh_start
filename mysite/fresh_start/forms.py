from django import forms


class ResourceForm(forms.Form):
    name = forms.CharField(label='Name/Organization', max_length=100)
    url = forms.URLField(label='Website')
