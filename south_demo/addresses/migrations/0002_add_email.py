
from south.db import db
from django.db import models
from addresses.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Contact.email'
        db.add_column('addresses_contact', 'email', models.EmailField(null=True, blank=True))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Contact.email'
        db.delete_column('addresses_contact', 'email')
        
    
    
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
