from django import forms
from money import models

# Inputs
class DatepickerInput(forms.widgets.DateInput):

    attrs = {'class' : 'datepicker'}

    def __init__(self):
        super(DatepickerInput,self).__init__(self.attrs)


# Forms
class EntryForm(forms.ModelForm):
    class Meta:
        exclude = ('user',)
        model = models.Entry
        widgets={
            'pay_date' : DatepickerInput(),
            'paid_date' : DatepickerInput(),
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

class EntryFilterForm(forms.Form):
    start_date = forms.CharField(max_length=20, widget=forms.widgets.TextInput(attrs={'class':'span2 datepicker'}))
    end_date = forms.CharField(max_length=20, widget=forms.widgets.TextInput(attrs={'class':'span2 datepicker'}))
