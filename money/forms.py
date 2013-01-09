from django import forms
from money import models

class EntryForm(forms.ModelForm):
    class Meta:
        model = models.Entry