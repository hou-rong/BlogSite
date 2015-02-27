from django.shortcuts import (render, get_object_or_404, get_list_or_404)
from Blog.models import *


def home(request):
    posts = Blog.objects.order_by('-updateTime')
    categorys = Category.objects.all()
    hotPassages = Blog.objects.order_by('-accessCount')[:10]
    timeMachine = Blog.objects
    return render(request, 'home.html', {'posts': posts, 'categorys': categorys, 'hotPassages': hotPassages})


def rank(request):
    pass


def about(request):
    pass


def archive(request, shortUrl):
    post = get_object_or_404(Blog, shortUrl=shortUrl)
    post.accessCount += 1
    post.save()
    categorys = Category.objects.all()
    hotPassages = Blog.objects.order_by('-accessCount')[:10]
    return render(request, 'archive.html', {'post': post, 'categorys': categorys, 'hotPassages': hotPassages})


def search(request):
    pass


# todo create python function to complate the page automaticly
# todo create <pre><code></code></pre> label to let highlight.js work
