from django.shortcuts import (render, get_object_or_404, get_list_or_404)
from Blog.models import *
import functools
from django.db.models import Q
import operator
import jieba.analyse


def home(request):
    posts = Blog.objects.order_by('-updateTime')
    categorys = getCategorysAndNumber()
    hotPassages = Blog.objects.order_by('-accessCount')[:10]
    timeMachines = getTimeMachines()
    return render(request, 'home.html', {'posts': posts, 'categorys': categorys,
                                         'hotPassages': hotPassages, 'timeMachines': timeMachines})


def rank(request):
    pass


def about(request):
    pass


def archive(request, shortUrl):
    post = get_object_or_404(Blog, shortUrl=shortUrl)
    post.accessCount += 1
    post.save()
    categorys = getCategorysAndNumber()
    hotPassages = Blog.objects.order_by('-accessCount')[:10]
    timeMachines = getTimeMachines()
    return render(request, 'archive.html',
                  {'post': post, 'categorys': categorys, 'hotPassages': hotPassages, 'timeMachines': timeMachines})


def search(request):
    query = request.POST['query']
    keys = jieba.analyse.extract_tags(query, len(query))
    if not keys:
        keys = query.split()
    titleCondition = functools.reduce(operator.and_, (Q(title__icontains=x) for x in keys))
    bodyCondition = functools.reduce(operator.and_, (Q(body__icontains=x) for x in keys))
    posts = (Blog.objects.filter(titleCondition) or Blog.objects.filter(bodyCondition)).order_by('-updateTime')
    # todo order by key word rank
    categorys = getCategorysAndNumber()
    hotPassages = Blog.objects.order_by('-accessCount')[:10]
    keyRank = '>'.join(keys)
    timeMachines = getTimeMachines()
    return render(request, 'search.html',
                  {'posts': posts, 'categorys': categorys, 'hotPassages': hotPassages,
                   'keyRank': keyRank, 'timeMachines': timeMachines})


def category(request, shortUrl):
    posts = Category.objects.get(shortUrl=shortUrl).category.order_by('-updateTime')
    title = Category.objects.get(shortUrl=shortUrl).title
    categorys = getCategorysAndNumber()
    hotPassages = Blog.objects.order_by('-accessCount')[:10]
    timeMachines = getTimeMachines()
    return render(request, 'category.html', {'posts': posts, 'categorys': categorys,
                                             'hotPassages': hotPassages, 'title': title, 'timeMachines': timeMachines})


def timeMachine(request, year, month):
    posts = get_list_or_404(Blog.objects.order_by('-updateTime'), createTime__year=year, createTime__month=month)
    categorys = getCategorysAndNumber()
    hotPassages = Blog.objects.order_by('-accessCount')[:10]
    timeMachines = getTimeMachines()
    return render(request, 'home.html', {'posts': posts, 'categorys': categorys,
                                         'hotPassages': hotPassages, 'timeMachines': timeMachines})


def tagView(request, shortUrl):
    posts = Tag.objects.get(shortUrl=shortUrl).blog_set.all()
    title = Tag.objects.get(shortUrl=shortUrl).title
    categorys = getCategorysAndNumber()
    hotPassages = Blog.objects.order_by('-accessCount')[:10]
    timeMachines = getTimeMachines()
    return render(request, 'category.html', {'posts': posts, 'categorys': categorys,
                                             'hotPassages': hotPassages, 'title': title, 'timeMachines': timeMachines})


def getCategorysAndNumber():
    showCategorys = []
    for i in Category.objects.all():
        showCategorys.append({'title': i.title, 'number': Blog.objects.filter(
            category__in=Category.objects.filter(title=i.title)).count(), 'shortUrl': i.shortUrl})
    showCategorys.sort(key=lambda x: x['number'], reverse=True)
    return showCategorys


def getTimeMachines():
    # get temporary dictionary
    temporaryTimeMachines = {}
    for i in Blog.objects.all():
        key = (i.createTime.year, i.createTime.month)
        if key not in temporaryTimeMachines:
            temporaryTimeMachines.update({key: 1})
        else:
            temporaryTimeMachines[key] += 1

    # format dictionary
    timeMachines = []
    for i in temporaryTimeMachines.keys():
        timeMachines.append(
            {'title': "%s年%s月" % (i[0], i[1]), 'number': temporaryTimeMachines[i], 'year': i[0],
             'month': i[1]})
    return timeMachines

    # 用字典表示，如果字典中有該名字的鍵值，數量加一，如果該字典里沒有該鍵值，創造該鍵，數量爲一


    # todo create <pre><code></code></pre> label to let highlight.js work
    # todo create page changing function
    # todo getCategorysAndNumber could be replace by a simple way
    # todo get user who visit this blog recently and where he come from
