from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Contact(models.Model):

	name 		= models.CharField(_('Name'),max_length=512)
	is_company	= models.BooleanField(_('Company'),default=False)
	image		= models.ImageField(_('Image'),blank=True)

	def __str__(self):
		return '%s[%s]'%(self.name,self.is_company)

class Addition(models.Model):
	contact 	= models.ForeignKey(Contact)

class Tel(Addition):
	tel_type 	= models.CharField(_('Tel Type'),max_length=128)
	number		= models.CharField(_('Number'),max_length=128)

	def __str__(self):
		return '[%s]%s'%(self.tel_type,self.number)		