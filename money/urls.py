from django.conf.urls import patterns, include, url
from money import views as views_money

urlpatterns = patterns('',
    url(r'^$', views_money.EntryList.as_view(), name='entry_list'),
    url(r'^entry/create$', views_money.EntryCreate.as_view(), name='entry_create'),
    url(r'^banks/$', views_money.BankList.as_view(), name='bank_list'),
    url(r'^banks/edit/(?P<pk>\d+)$', views_money.BankList.as_view(), name='bank_edit'),
    url(r'^accounts/$', views_money.AccountList.as_view(), name='account_list'),
    url(r'^people/$', views_money.PersonList.as_view(), name='person_list'),
    url(r'^people/edit/(?P<pk>\d+)$', views_money.PersonList.as_view(), name='person_edit'),

)
