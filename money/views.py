from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin
from django.core.urlresolvers import reverse_lazy
from money import generic
from money import settings
from money.models import Entry, Bank, Account, Person
from money import forms
from money.utils import last_day_of_this_month
from datetime import datetime

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

class EntryList(generic.RestrictedListView, FormMixin):
    model=Entry
    form_class=forms.EntryFilterForm

    def get(self, request, *args, **kwargs):
        today = datetime.today().date()
        if request.GET:
            self.start_date = datetime.strptime(request.GET.get('start_date'), settings.DATE_FORMAT)
            self.end_date = datetime.strptime(request.GET.get('end_date'), settings.DATE_FORMAT)
        else:
            self.start_date = today.replace(day=1)
            self.end_date = last_day_of_this_month(today)

        return super(EntryList, self).get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Entry.objects.filter(pay_date__range=(self.start_date, self.end_date))
        return queryset

    def get_initial(self):
        initial = super(EntryList, self).get_initial()
        initial['start_date'] = datetime.strftime(self.start_date, settings.DATE_FORMAT)
        initial['end_date'] = datetime.strftime(self.end_date, settings.DATE_FORMAT)
        return initial

    def get_context_data(self, **kwargs):
        context = super(EntryList, self).get_context_data(**kwargs)
        context['form'] = self.get_form(self.get_form_class())
        return context

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
