from django import forms
from money import models

class EntryForm(forms.ModelForm):
    class Meta:
        exclude = ('user',)
        model = models.Entry
        widgets={
            'pay_date' : forms.TextInput(attrs={'class': 'datepicker'}),
            'paid_date' : forms.TextInput(attrs={'class': 'datepicker'}),
        }

class BankForm(forms.ModelForm):
    class Meta:
        exclude = ('user',)
        model = models.Bank

class AccountForm(forms.ModelForm):
    class Meta:
        exclude = ('user',)
        model = models.Account

class PersonForm(forms.ModelForm):
    class Meta:
        exclude = ('user',)
        model = models.Person