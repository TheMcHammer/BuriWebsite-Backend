from django.db import models
from django.core.urlresolvers import reverse

class Client(models.Model):
	company = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	phone_num = models.IntegerField()
	address = models.CharField(max_length=300)
	email = models.CharField(max_length=200)
	
	def get_absolute_url(self):
		return reverse('get_quote:detail', kwargs={'pk':self.pk})
		
	def __str__(self):
		return self.company + ' - ' + self.name + ' - ' + self.email
	
class Commodity(models.Model):
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	commodity_type = models.CharField(max_length=200)
	quantity = models.CharField(max_length=300)
	packing_type = models.CharField(max_length=300)
	is_clear_forward = models.BooleanField(default=False)
	
	def __str__(self):
		return self.commodity_type + ' - ' + self.quantity
		
class Transport(models.Model):
	commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
	pick_from = models.CharField(max_length=300)
	deliver_to = models.CharField(max_length=300)
	
	