# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('src.main.views',
    url(r'^$', 'index', name='index'),
    url(r'^index/$', 'first_page', name='first_page'),
    url(r'^index/(?P<slug>\w+)\.html/$', 'book_redirect'),
    url(r'^search/$', 'search', name='search'),
    url(r'^feedback/$', 'feedback', name='feedback'),
    url(r'^thanks/$', 'thanks', name='thanks'),
    url(r'^markdown_preview/$', 'markdown_preview', name='markdown_preview'),
    url(r'^test_error_email/', 'test_error_email'),
    url(r'^lang/(?P<lang_code>[a-z]{2})/$', 'lang', name='lang'),
    url(r'^(?P<slug>\w+)\.html', 'page', name='page')
)
