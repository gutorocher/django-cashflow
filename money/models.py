from django.db import models
from django.contrib.auth.models import User

class IdentModel(models.Model):
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False),

    class Meta:
        abstract = True

class Account(IdentModel):
    TYPE_CHOICES = (
        ('D', 'Debit'),
        ('C', 'Credit'),
    )

    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    status = models.BooleanField()

    def __unicode__(self):
        return self.name

class Bank(IdentModel):
    name = models.CharField(max_length=100)
    limit = models.FloatField(default=0)

    def __unicode__(self):
        return self.name

class Person(IdentModel):
    name = models.CharField(max_length=100)
    doc = models.CharField(max_length=20,blank=True, null=True)
    status = models.BooleanField()
    default_account = models.ForeignKey(Account, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Entry(IdentModel):
    account = models.ForeignKey(Account)
    bank = models.ForeignKey(Bank)
    person = models.ForeignKey(Person)
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    pay_date = models.DateField()
    paid_date = models.DateField(blank=True, null=True)
    doc = models.CharField(max_length=20, blank=True, null=True)
    check = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=1, default=0)

    def __unicode__(self):
        return self.name
