
from south.db import db
from django.db import models
from accounts.models import *

class Migration:
    depends_on = (
        ('addresses', '0003_fix_email_data'),
    )
    
    def forwards(self, orm):
        
        # Adding model 'UserProfile'
        db.create_table('accounts_userprofile', (
            ('bio', models.TextField()),
            ('address_book', models.ForeignKey(orm['addresses.Book'])),
            ('id', models.AutoField(primary_key=True)),
            ('user', models.OneToOneField(orm['auth.User'])),
        ))
        db.send_create_signal('accounts', ['UserProfile'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'UserProfile'
        db.delete_table('accounts_userprofile')
        
    
    
    models = {
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'accounts.userprofile': {
            'address_book': ('models.ForeignKey', ["'addresses.Book'"], {}),
            'bio': ('models.TextField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'user': ('models.OneToOneField', ["'auth.User'"], {})
        },
        'addresses.book': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        }
    }
    
    complete_apps = ['accounts']
