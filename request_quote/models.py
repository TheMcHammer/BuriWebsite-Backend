from django.db import models
from django.core.urlresolvers import reverse

class Quote(models.Model):
	company = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	phone_num = models.IntegerField()
	address = models.CharField(max_length=300)
	email = models.CharField(max_length=200)
	commodity_type = models.CharField(max_length=200)
	quantity = models.CharField(max_length=300)
	packing_type = models.CharField(max_length=300)
	is_clear_forward = models.BooleanField(default=False)
	pick_from = models.CharField(max_length=300)
	deliver_to = models.CharField(max_length=300)