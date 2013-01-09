from django.views.generic.list import ListView
from money.models import Entry

class EntryList(ListView):
	model=Entry
