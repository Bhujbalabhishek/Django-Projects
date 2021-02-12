from django.shortcuts import render, get_object_or_404, redirect
from .models import Posts
from django.http import HttpResponse 
from .forms import Post_Form
from django.utils import timezone
from django.core import serializers
# Create your views here.


def post_list(request):
    posts = Posts.objects.order_by('-date_posted')
    return render(request, 'posts/posts_list.html', {'posts': posts})



def post_detail(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = Post_Form(request.POST)
        if form.is_valid():
            post = form.save()
            post.date_posted = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = Post_Form()
    return render(request, 'posts/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    if request.method == "POST":
        form = Post_Form(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            post.date_posted = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = Post_Form(instance=post)
    return render(request, 'posts/post_edit.html', {'form': form})



def serialize(request):
    ser = serializers.serialize('json', Posts.objects.all(), fields=('text','content','id','date_posted'))

    return render(request, 'posts/serialize.html', {'ser': ser})
