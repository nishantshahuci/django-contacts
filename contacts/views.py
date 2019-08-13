# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from contacts.models import Contact, Address

@login_required
def contacts(request):
    ''' Show the list of contacts '''
    # get the contacts the current user owns
    contacts = Contact.objects.filter(owned_by = request.user)
    return render(request, 'contacts/index.html', {
        'contacts': contacts,
        'count': contacts.count()
    })

@login_required
def edit(request, contact_id=None):
    ''' Show the edit page for the current contact, or create a new one '''

    exists = False if contact_id == None else True

    if request.method == 'POST':

        # save data
        contact = None

        street = request.POST.get('street')
        apartment = request.POST.get('apartment')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')

        owned_by = request.user
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        email_address = request.POST.get('email_address')

        if exists:
            # if the contact already exists, update it - else add it

            contact = Contact.objects.get(id=contact_id)
            address = Address.objects.get(id=contact.address.id)

            address.street = street
            address.apartment = apartment
            address.city = city
            address.state = state
            address.zip = zip
            address.save()

            contact.first_name = first_name
            contact.last_name = last_name
            contact.phone_number = phone_number
            contact.email_address = email_address
            contact.address = address
            contact.save()

        else:
            # add the address
            address = Address(street=street,
                              apartment=apartment,
                              city=city,
                              state=state,
                              zip=zip)
            address.save()

            # add the contact
            contact = Contact(owned_by=owned_by,
                              first_name=first_name,
                              last_name=last_name,
                              phone_number=phone_number,
                              email_address=email_address,
                              address=address)
            contact.save()

        return redirect('contacts:contacts')

    else:
        if contact_id == None:
            return render(request, 'contacts/edit.html', {
                'contact': None,
                'exists': exists
            })
        else:
            contact = Contact.objects.get(id=contact_id)
            # check if contact belongs to logged in user
            if contact.owned_by == request.user:
                exists = True
                return render(request, 'contacts/edit.html', {
                    'contact': contact,
                    'exists': exists
                })
            else:
                return redirect('contacts:contacts')

@login_required
def delete(request, contact_id):
    ''' Delete the contact if it belongs to the user '''
    try:
        contact = Contact.objects.get(id=contact_id)
        if contact.owned_by == request.user:
            contact.address.delete()
            contact.delete()
            return redirect('contacts:contacts')
    except:
        return redirect('contacts:contacts')

@login_required
def search(request):
    ''' Filter contact list '''

    if request.method == 'POST':
        # get search term
        search_term = request.POST.get('search')

        # filter on first name or last name contains
        contacts = Contact.objects.filter(owned_by=request.user).filter(first_name__icontains=search_term) | Contact.objects.filter(owned_by=request.user).filter(last_name__icontains=search_term)
        
        return render(request, 'contacts/index.html', {
            'contacts': contacts,
            'count': contacts.count()
        })
