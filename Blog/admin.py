from django.contrib import admin
from .models import *
import uuid


def getShortUrl():
    shortUrl = str(uuid.uuid4()).replace('-', '')[:10]
    try:
        Blog.objects.get(shortUrl=shortUrl)
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
        ('Advanced options', {
            'classes': ('Blog', ),
            'fields': ('tags', ),
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.shortUrl = getShortUrl()
        obj.save()

# todo create tags by textRank
# todo jieba can't use in python3
# todo remove code in fields to make it can use textRank
# todo use openCC to change language in blog

# class BlogAdmin(admin.ModelAdmin):
# list_display = ['title', 'createTime', 'updateTime']
#
# class Meta:
# __module__ = Blog


admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)
admin.site.register(Category)

# todo create a beautiful admin page