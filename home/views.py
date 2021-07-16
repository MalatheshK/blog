from django import forms
from home.forms import BlogForm
from home.models import Blogs
from django.shortcuts import render
from .models import Blogs
from .forms import BlogForm


# Create your views here.
def index(request):
    obj = Blogs.objects.all
    context = {
        'obj':obj
    }
    return render(request,'home.html',context)

def post_view(request):
    context = {}

    form = BlogForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = BlogForm()

    context['form']=form
    return render(request, 'post.html', context)
