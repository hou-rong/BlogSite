from django.contrib import admin
from .models import *
import uuid
import jieba.analyse


def getShortUrl(Class):
    shortUrl = str(uuid.uuid4()).replace('-', '')[:10]
    try:
        Class.objects.get(shortUrl=shortUrl)
        getShortUrl()
    except:
        return shortUrl


class BlogAdmin(admin.ModelAdmin):
    list_per_page = 8
    list_display = ('title', 'updateTime', 'createTime', 'shortUrl', 'accessCount')
    search_fields = ('title', 'body')
    fieldsets = (
        (None, {
            'fields': (('title', 'category', ), 'body',),
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.shortUrl = getShortUrl(Blog)
        obj.save()
        title = obj.title
        body = request.POST['body']
        a = Blog.objects.get(title=title)
        a.tags.clear()
        keyWords = jieba.analyse.extract_tags(body, int(len(body) / 150))
        for i in keyWords:
            try:
                tag = Tag.objects.get(title=i)
            except:
                tag = Tag(title=i, shortUrl=getShortUrl(Tag))
                tag.save()
            a.tags.add(tag)
        obj.save()


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'shortUrl',)
    fieldsets = (
        (None, {
            'fields': ('title',),
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.shortUrl = getShortUrl(Category)
        obj.save()


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'shortUrl',)
    fieldsets = (
        (None, {
            'fields': ('title',),
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.shortUrl = getShortUrl(Tag)
        obj.save()


# todo use openCC to change language in blog

# class BlogAdmin(admin.ModelAdmin):
# list_display = ['title', 'createTime', 'updateTime']
#
# class Meta:
# __module__ = Blog


admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)
admin.site.register(Category, CategoryAdmin)

# todo create a beautiful admin page