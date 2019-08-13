# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.db import models

# Model to store user addresses
class Address(models.Model):
    street = models.CharField(max_length=254)
    apartment = models.CharField(max_length=10, null=True)
    city = models.CharField(max_length=254)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=10)

    def __str__(self):
        if self.apartment:
            return '{} Apt. {}, {}, {} - {}'.format(self.street, self.apartment, self.city, self.state, self.zip)
        else:
            return '{}, {}, {} - {}'.format(self.street, self.apartment, self.city, self.state, self.zip)

# Model to store contact information
class Contact(models.Model):
    owned_by = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=10)
    email_address = models.CharField(max_length=254)
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
