from django import forms


class PostForm(forms.Form):
    author = forms.CharField(required=False)
    message = forms.CharField()
