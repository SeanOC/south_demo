
from south.db import db
from django.db import models
from addresses.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Contact'
        db.create_table('addresses_contact', (
            ('book', models.ForeignKey(orm.Book)),
            ('first_name', models.CharField(max_length=100)),
            ('last_name', models.CharField(max_length=100)),
            ('id', models.AutoField(primary_key=True)),
        ))
        db.send_create_signal('addresses', ['Contact'])
        
        # Adding model 'Book'
        db.create_table('addresses_book', (
            ('id', models.AutoField(primary_key=True)),
            ('name', models.CharField(max_length=100)),
        ))
        db.send_create_signal('addresses', ['Book'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Contact'
        db.delete_table('addresses_contact')
        
        # Deleting model 'Book'
        db.delete_table('addresses_book')
        
    
    
    models = {
        'addresses.contact': {
            'book': ('models.ForeignKey', ['Book'], {}),
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
