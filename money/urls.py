from django.conf.urls import patterns, include, url
from money import views as views_money

urlpatterns = patterns('',
    url(r'^$', views_money.EntryList.as_view(), name='entry_list'),
)
