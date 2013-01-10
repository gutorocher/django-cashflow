from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, ModelFormMixin, ProcessFormView
from django.core.urlresolvers import reverse_lazy
from money.generic import ModelFormWithListView
from money.models import Entry, Bank, Account, Person
from money import forms

class EntryList(ListView):
    model=Entry

class EntryCreate(CreateView):
    model=Entry
    form_class=forms.EntryForm
    success_url = reverse_lazy('entry_list')

class BankList(ModelFormWithListView):
    model=Bank
    form_class=forms.BankForm
    success_url = reverse_lazy('bank_list')

class AccountList(ModelFormWithListView):
    model=Account
    form_class=forms.AccountForm
    success_url = reverse_lazy('account_list')

class PersonList(ModelFormWithListView):
    model=Person
    form_class=forms.PersonForm
    success_url = reverse_lazy('person_list')
