from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User')
    bio = models.TextField()
    address_book = models.ForeignKey('addresses.Book')
    
    def __unicode__(self):
        return u"%s's profile" % self.user
        