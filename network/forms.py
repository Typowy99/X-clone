from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(required=True,
        widget=forms.Textarea(
            attrs={'class': 'form-label form-textarea',}), 
                label=False)

    class Meta:
        model = Post
        exclude = ("post_author", 'likes',)