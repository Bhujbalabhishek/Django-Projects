from django import forms

from .models import Posts

class Post_Form(forms.ModelForm):
    
    class Meta:
        model = Posts
        fields = ("title","content")
