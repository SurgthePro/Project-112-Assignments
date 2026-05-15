from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
       # fields = ["title", "subtitle", "body", "status", "options"]
        fields = ["title", "subtitle", "body", "status"]
        widgets = {
            "options": forms.RadioSelect()
        }