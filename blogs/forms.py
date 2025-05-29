from django import forms

from .models import Blog, Post

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = {'name'}
        labels = {'name': ''}

class PostForm(forms.ModelForm):

    blog = forms.ModelChoiceField(queryset=Blog.objects.all(),
                                  empty_label="Select a blog category")

    class Meta:
        model = Post
        fields = ['blog', 'title', 'body']
        labels = {'title': 'Post Title', 'body': ''}
        widgets = {
                'body': forms.Textarea(attrs={'cols': 80})
                }
