# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView

from zinnia.sitemaps import TagSitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import AuthorSitemap

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()


handler404 = 'django.views.defaults.page_not_found'
handler403 = 'django.views.defaults.permission_denied'

urlpatterns = patterns('',
    url(r'^guard/doc/', include('django.contrib.admindocs.urls')),
    url(r'^guard/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url='/blog/')),
    url(r'^blog/', include('zinnia.urls')),
    url(r'^blog/comments/', include('django.contrib.comments.urls')),
    url(r'^', include('zinnia.urls.capabilities')),
    url(r'^blog/search/', include('zinnia.urls.search')),
    url(r'^blog/sitemap/', include('zinnia.urls.sitemap')),
    url(r'^blog/trackback/', include('zinnia.urls.trackback')),
    url(r'^blog/tags/', include('zinnia.urls.tags')),
    url(r'^blog/feeds/', include('zinnia.urls.feeds')),
    url(r'^blog/random/', include('zinnia.urls.random')),
    url(r'^blog/authors/', include('zinnia.urls.authors')),
    url(r'^blog/categories/', include('zinnia.urls.categories')),
    url(r'^blog/comments/', include('zinnia.urls.comments')),
    url(r'^blog/', include('zinnia.urls.entries')),
    url(r'^blog/', include('zinnia.urls.archives')),
    url(r'^blog/', include('zinnia.urls.shortlink')),
    url(r'^blog/', include('zinnia.urls.quick_entry')),
    url(r'^blog/xmlrpc/$', 'django_xmlrpc.views.handle_xmlrpc'),
)

urlpatterns += patterns('',
                       url(r'^velho/$',
                           TemplateView.as_view(template_name='pages/home.html'),
                           name="home"),
                       url(r'^velho_about/$',
                           TemplateView.as_view(template_name='pages/about.html'),
                           name="about"),

                       # Uncomment the next line to enable the admin:
                       #url(r'^admin/', include(admin.site.urls)),

                       # User management
                       url(r'^users/', include("users.urls", namespace="users")),
                       url(r'^accounts/', include('allauth.urls')),

                       # Uncomment the next line to enable avatars
                       url(r'^avatar/', include('avatar.urls')),

                       # Your stuff: custom urls go here

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



sitemaps = {
    'tags': TagSitemap,
    'blog': EntrySitemap,
    'authors': AuthorSitemap,
    'categories': CategorySitemap
}

urlpatterns += patterns(
    'django.contrib.sitemaps.views',
    url(r'^sitemap.xml$', 'index',
        {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', 'sitemap',
        {'sitemaps': sitemaps}),
)

urlpatterns += patterns(
    '',
    url(r'^403/$', 'django.views.defaults.permission_denied'),
    url(r'^404/$', 'django.views.defaults.page_not_found'),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT})
    )
