from django.db import models

class Contact(models.Model):
	first_name = models.CharField(max_length=100)
	second_name = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	county = models.CharField(max_length=200)
	town = models.CharField(max_length=50)
	email = models.CharField(max_length=100)
	comment =models.CharField(max_length=500)