from django.db import models

# Create your models here.
class Contact(models.Model):

	name 		= models.CharField(max_length=256)
	is_company	= models.BooleanField()

	def __str__(self):
		return "Contect object"