from django import forms
from money import models

class EntryForm(forms.ModelForm):
    class Meta:
        model = models.Entry

class BankForm(forms.ModelForm):
	class Meta:
		model = models.Bank

class AccountForm(forms.ModelForm):
	class Meta:
		model = models.Account