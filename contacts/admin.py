# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from contacts.models import Contact, Address

# Register your models here.
admin.site.register(Contact)
admin.site.register(Address)
