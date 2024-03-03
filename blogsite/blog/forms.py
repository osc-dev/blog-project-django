from django import forms
from blog.models import Post,Comment
from django_quill.fields import QuillField

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text')

    widgets = {
        'title': forms.TextInput(attrs={'class':'textinputclass'}),
        'text': QuillField()
    }    

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')

    widgets = {
        'author': forms.TextInput(attrs={'class':'textinputclass'}),
        'text': QuillField()
    }
