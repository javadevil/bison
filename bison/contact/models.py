from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Contact(models.Model):

	f_name 		= models.CharField(_('First Name'),max_length=256)
	s_name		= models.CharField(_('Last Name'),max_length=256,blank=True)
	prefix		= models.CharField(_('Prefix'),max_length=64,blank=True)

	is_company	= models.BooleanField(_('Company'),default=False)

	def __str__(self):
		return '%s %s,%s'%(self.f_name,self.s_name,self.prefix)