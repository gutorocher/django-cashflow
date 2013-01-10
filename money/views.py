from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, ModelFormMixin, ProcessFormView, DeleteView
from django.core.urlresolvers import reverse_lazy
from money import generic
from money.models import Entry, Bank, Account, Person
from money import forms

class EntryList(generic.RestrictedListView):
    model=Entry

class EntryCreate(generic.RestrictedCreateView):
    model=Entry
    form_class=forms.EntryForm
    success_url = reverse_lazy('entry_list')

class BankList(generic.ModelFormWithListView):
    model=Bank
    form_class=forms.BankForm
    success_url = reverse_lazy('bank_list')

class BankDelete(generic.RestrictedDeleteView):
    model=Bank
    success_url = reverse_lazy('bank_list')

class AccountList(generic.ModelFormWithListView):
    model=Account
    form_class=forms.AccountForm
    success_url = reverse_lazy('account_list')

class PersonList(generic.ModelFormWithListView):
    model=Person
    form_class=forms.PersonForm
    success_url = reverse_lazy('person_list')
