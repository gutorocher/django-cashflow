from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from money import views as views_money

urlpatterns = patterns('',

    #auth
    url(r'^$', 'django.contrib.auth.views.login', name='user_login'),
    url(r'^login$', 'django.contrib.auth.views.login', name='user_login'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': reverse_lazy('user_login')} ,name='user_logout'),

    #app
    url (r'^dashboard$',views_money.DashBoard.as_view(), name='dashboard'),
    url(r'^entries$', views_money.EntryList.as_view(), name='entry_list'),
    url(r'^entries/create$', views_money.EntryCreate.as_view(), name='entry_create'),

    url(r'^banks/$', views_money.BankList.as_view(), name='bank_list'),
    url(r'^banks/edit/(?P<pk>\d+)$', views_money.BankList.as_view(), name='bank_edit'),
    url(r'^banks/delete/(?P<pk>\d+)$', views_money.BankDelete.as_view(), name='bank_delete'),

    url(r'^accounts/$', views_money.AccountList.as_view(), name='account_list'),
    url(r'^accounts/edit/(?P<pk>\d+)$', views_money.AccountList.as_view(), name='account_edit'),

    url(r'^people/$', views_money.PersonList.as_view(), name='person_list'),
    url(r'^people/edit/(?P<pk>\d+)$', views_money.PersonList.as_view(), name='person_edit'),

)
