
from south.db import db
from django.db import models
from addresses.models import *

class Migration:
    
    def forwards(self, orm):
        "Write your forwards migration here"
    
    
    def backwards(self, orm):
        "Write your backwards migration here"
    
    
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
