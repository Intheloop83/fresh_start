from django import forms


class ResourceForm(forms.Form):
    name = forms.CharField(label='Organization/Name', max_length=100)
    url = forms.URLField(label='Website')
