
from south.db import db
from django.db import models
from django.db.models import Q
from addresses.models import *

class Migration:
    
    def forwards(self, orm):
        Contact = orm['addresses.contact']
        empty_emails = Contact.objects.filter(Q(email__isnull=True)|Q(email=''))
        for contact in empty_emails:
            print "Fixing %s" % contact
            contact.email = 'fixme@somedomain.com'
            contact.save()
    
    
    def backwards(self, orm):
        Contact = orm['addresses.contact']
        fixed_contacts = Contact.objects.filter(email='fixme@somedomain.com')
        for contact in fixed_contacts:
            contact.email = None
            contact.save()
    
    
    models = {
        'addresses.contact': {
            'book': ('models.ForeignKey', ['Book'], {}),
            'email': ('models.EmailField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('models.CharField', [], {'max_length': '100'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('models.CharField', [], {'max_length': '100'})
        },
        'addresses.book': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '100'})
        }
    }
    
    complete_apps = ['addresses']
