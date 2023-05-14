from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    title = forms.CharField(help_text='maskymalnie 200 znaków')
    class Meta:
        model = Post
        fields = ['title', 'text', 'image']
