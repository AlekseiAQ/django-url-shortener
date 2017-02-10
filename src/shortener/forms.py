from django import forms


class SubminUrlForm(forms.Form):
    url = forms.CharField(label="Submit your URL")
