from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=200)
	price = models.IntegerField(max_length=10)

