from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, ModelFormMixin, ProcessFormView
from django.core.urlresolvers import reverse_lazy
from money.generic import ModelFormWithListView
from money.models import Entry, Bank, Account
from money import forms

class EntryList(ListView):
	model=Entry

class EntryCreate(CreateView):
	model=Entry
	form_class=forms.EntryForm
	success_url = reverse_lazy('entry_list')

class BankList(ListView, ModelFormMixin, ProcessFormView):
	model=Bank
	form_class=forms.BankForm
	success_url = reverse_lazy('bank_list')

	def post(self, request, *args, **kwargs):
		try:
			self.object = self.get_object()
		except:
			self.object = None
		return super(BankList, self).post(request, *args, **kwargs)

	def get_context_data(self, **kwargs):

		self.object_list = self.get_queryset()

		try:
			self.object = self.get_object()
		except:
			self.object = None

		kwargs.update({
			'object_list' : self.object_list,
			'form' : self.get_form(self.get_form_class()),
			'object' : self.object
		})

		return super(BankList, self).get_context_data(**kwargs)

class AccountList(ModelFormWithListView):
	model=Account
	form_class=forms.AccountForm
	success_url = reverse_lazy('account_list')
