from django import forms
from django.forms import fields
from .models import Blogs

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = "__all__"