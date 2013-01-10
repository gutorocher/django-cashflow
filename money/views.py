from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from money import generic
from money.models import Entry, Bank, Account, Person
from money import forms

class DashBoard(generic.LoginRequired, TemplateView):
    template_name='money/dashboard.html'

    def get_graph_data(self):
        output = []
        output.append(['01/01',1000, 1100])
        output.append(['02/01',2500, 2000])
        output.append(['03/01',3000, 3500])
        output.append(['04/01',1500, 1500])
        output.append(['05/01',1700, 2000])
        output.append(['06/01',5800, 6000])
        output.append(['07/01',3400, 3500])
        output.append(['08/01',4000, 2000])
        output.append(['09/01',1500, 2000])
        return output

    def get_context_data(self, **kwargs):
        context = super(DashBoard, self).get_context_data(**kwargs)
        context['graph_01'] = self.get_graph_data()
        return context

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
