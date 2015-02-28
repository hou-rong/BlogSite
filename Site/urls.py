from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'Site.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^archive/(?P<shortUrl>\w+)/', 'Blog.views.archive', name='archive'),
                       url(r'^search/', 'Blog.views.search', name='search'),
                       url(r'^category/(?P<shortUrl>\w+)/', 'Blog.views.category', name='category'),
                       url(r'^$', 'Blog.views.home', name='home'),
)
