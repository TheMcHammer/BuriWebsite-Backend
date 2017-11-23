from django.db import models
from django.core.urlresolvers import reverse

class Contact(models.Model):
	first_name = models.CharField(max_length=100)
	second_name = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	county = models.CharField(max_length=200)
	town = models.CharField(max_length=50)
	email = models.CharField(max_length=100)
	comment = models.TextField(max_length=500)
	
	def get_absolute_url(self):
		return reverse('contact_add')
		
	def __str__(self):
		return self.second_name + ' - ' + self.address + ' - ' + self.email
	