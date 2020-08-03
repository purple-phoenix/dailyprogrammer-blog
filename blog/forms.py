from django.forms import ModelForm
from blog.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'content', 'status', 'picture']
