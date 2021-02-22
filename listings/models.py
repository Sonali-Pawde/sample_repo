

# Create your models here.
from django.db import models
from datetime import datetime
from realtors.models import Realtor

# Create your models here.


class Listing(models.Model):
	realtor = models.ForeignKey(Realtor, on_delete = models.DO_NOTHING)
	title = models.CharField(max_length = 200)
	address = models.CharField(max_length = 200)
	city = models.CharField(max_length = 100)
	state = models.CharField(max_length = 100)
	zipcode = models.CharField(max_length = 200)
	description = models.TextField(blank=True)
	price = models.IntegerField()
	bedrooms = models.IntegerField()
	bathrooms = models.IntegerField()
	garage = models.IntegerField(default = 0)
	sqft = models.IntegerField()
	lot_size = models.DecimalField(max_digits = 2, decimal_places = 1)
	is_published = models.BooleanField(default = True)
	list_date = models.DateTimeField(default=datetime.now)
	photo_main = models.ImageField(upload_to = 'listings/')
	photo_1 = models.ImageField(upload_to = 'listings/', blank = True)
	photo_2 = models.ImageField(upload_to = 'listings/', blank = True)
	photo_3 = models.ImageField(upload_to = 'listings/', blank = True)
	photo_4 = models.ImageField(upload_to = 'listings/', blank = True)
	photo_5 = models.ImageField(upload_to = 'listings/', blank = True)
	photo_6 = models.ImageField(upload_to = 'listings/', blank = True)

	def __str__(self):
		return self.title

class Contact(models.Model):
	listing = models.CharField(max_length=200)
	listing_id = models.IntegerField()
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=100, blank=True)
	message = models.TextField(blank=True)
	contact_date = models.DateTimeField(default=datetime.now)
	user_id = models.IntegerField(blank=True)

	def __str__(self):
		return self.name