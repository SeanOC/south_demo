from django.db import models


class Book(models.Model):
	name = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.name

class Contact(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	book = models.ForeignKey(Book)
	
	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)