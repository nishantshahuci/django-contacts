from django.conf.urls import url
from contacts import views

app_name = 'contacts'

urlpatterns = [
    url(r'^$', views.contacts, name='contacts'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^edit/(?P<contact_id>[0-9]+)?/$', views.edit, name='edit'),
    url(r'^delete/(?P<contact_id>[0-9]+)/$', views.delete, name='delete'),
    url(r'^search/$', views.search, name='search')
]
