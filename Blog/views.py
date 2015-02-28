from django.shortcuts import (render, get_object_or_404, get_list_or_404)
from Blog.models import *
import functools
from django.db.models import Q
import operator
import jieba.analyse


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
    query = request.POST['query']
    keys = jieba.analyse.extract_tags(query, len(query))
    if not keys:
        keys = query.split()
    titleCondition = functools.reduce(operator.and_, (Q(title__icontains=x) for x in keys))
    bodyCondition = functools.reduce(operator.and_, (Q(body__icontains=x) for x in keys))
    posts = (Blog.objects.filter(titleCondition) or Blog.objects.filter(bodyCondition)).order_by('updateTime')
    # todo order by key word rank
    categorys = Category.objects.all()
    hotPassages = Blog.objects.order_by('-accessCount')[:10]
    keyRank = '>'.join(keys)
    timeMachine = Blog.objects
    return render(request, 'search.html',
                  {'posts': posts, 'categorys': categorys, 'hotPassages': hotPassages, 'keyRank': keyRank})


# todo create <pre><code></code></pre> label to let highlight.js work
