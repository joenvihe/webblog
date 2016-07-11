from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta: # toma como modelo del formulario la clase Post
        model = Post
        fields = ('title', 'text',)