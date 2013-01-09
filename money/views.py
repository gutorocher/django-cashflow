from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from money.models import Entry
from money import forms

class EntryList(ListView):
	model=Entry

class EntryCreate(CreateView):
	model=Entry
	form_class=forms.EntryForm
	success_url = reverse_lazy('entry_list')